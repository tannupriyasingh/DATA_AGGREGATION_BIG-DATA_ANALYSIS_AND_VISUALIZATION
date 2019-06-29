#!/usr/bin/python3

import gzip
import boto3
import botocore
import tempfile
from requests import get
import json
import warc
from langdetect import detect
import re
import os

# The list of keywords that will be used to filter out the articles.
topic_words = [
    'Souther Border', 'Border Wall', 'Green Card', 'Alexandria Ocasio-Cortez',
    'Green New Deal', 'Climate Change', 'Environmental Protection Agency', 'Obamacare', 'Medicaid', 'Medicare',
    '2020 elections', "Beto O'Rourke", 'Bernie Sanders', 'Elizabeth Warren', 'joe biden', 'Kamala Harris',
    'william barr', 'russia inquiry', 'Mueller report', 'N.R.A', 'Gun Law', 'Gun Violence', 'Mass Shootings'
]
pages = []
# We setup the resource to access the S3 instance
resource = boto3.resource('s3')
# The client access to modify or create files on S3
client = boto3.client('s3')
cc_bucket = resource.Bucket('commoncrawl')

# We access the public bucket of commoncrawl and pick up a segment of the commoncrawl
# From march of 2019, We picked the first segement available as each segment contains
# 500+ files and therefore is enough for our data.
files = list(cc_bucket.objects.filter(Prefix='crawl-data/CC-MAIN-2019-13/segments/1552912206677.94/wet'))
# my_cc_bucket = boto3.resource('cse-cc')


def check_for_keywords(content):
    # The WET file is written to a temporary file.
    test_file = open('test1.warc.wet', "w")
    test_file.write(content)
    test_file.close()
    cc_corpus = []
    # We do not want articles with URLs containing these words as they will not contain any valuable data.
    not_relevant_urls = ['login', 'calendar', 'archive', 'forum', 'tag', 'wordpress', 'blog', 'bit.ly', 'yelp', 'video', 'edu', '.ie', '.nl', '.ca', 'category', '.cn', ]
    # We are using the WARC-WET Package to open  up the WET file and start reading each record.
    with warc.open('test1.warc.wet') as file:
        print("inside the file")
        i = 0
        for record in file:
            i += 1
            try:
                # We make sure first that the record's URI doesn't contain the one of the above words
                if not any(w in record['WARC-Target-URI'].lower() for w in not_relevant_urls):
                    # We extract the data from it.
                    lines = record.payload.read().decode('UTF-8')
                    try:
                        # We make sure that it is english as we are only looking for
                        # English articles
                        if detect(lines) == 'en':
                            # If the article contains our keyword then we are going to store it.
                            if any(word in lines for word in topic_words):
                                    cc_corpus.append(lines)
                                    print(i, len(cc_corpus))
                    except Exception:
                        continue
            except Exception:
                continue
    # After going through the entire record, we will remove the test file and return the corpus
    if len(cc_corpus) > 0:
        os.remove('test1.warc.wet')
        return cc_corpus

# Once we have the list of the files we go thorugh each key and get the
# WET object from S3 that we can use to parse.
for file in files:
    clean_text = ''
    print(file_name)
# The WET ZIP is stored to a temp file
    with open('zip_file.wet.gz', "wb") as zipper:
        cc_bucket.Object(file.key).download_fileobj(zipper)
        print("file downloaded")
        zipper.close()
# The zip is openned and then we send it to our function to find the relvant
# Articles for our keywords.
    file_content = gzip.open('zip_file.wet.gz', 'r').read().decode('utf-8')
    print("written to test file")
    corpus = check_for_keywords(file_content)

# Once we have gathered all the articles needed from the WET file.
# We know save it to a text file for further processing.
# We also add an attachment as to how many articles did we gather from this file.
    if len(corpus) > 0:
        store_file_name = file.key.split('/')[5].split('.')[0] + '.txt'
        saving_file = open(store_file_name, "w")
        clean_text = '\n'.join(corpus)
        saving_file.write(clean_text)
        saving_file.close()
        client.upload_file(store_file_name, 'cse-cc', store_file_name)
    # We delete the zip file in the end as well.
    os.remove('zip_file.wet.gz')
