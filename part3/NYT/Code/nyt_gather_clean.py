#!/usr/bin/env python

import glob
import os
import json
import re

# We are importing all the files that contain our raw NYT data
files_list = glob.glob(os.path.join(os.getcwd(), "../nyt_raw_data/nyt_final_json_*.txt"))


# We will basic clean up the nyt data with things are unique to it, like URLs and dots between our keywords.
# And then add it to the new corpus.
# We are also checking that every article is unique across the board and the no article is repeated. 
def nyt_clean_up(article):
    if not article['id'] in nyt_ids:
        article['full_text'] = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', article['full_text'], flags=re.MULTILINE)
        article['full_text'] = article['full_text'].replace(".", '')
        nyt_corpus.append(article['full_text'])
        nyt_ids.append(article['id'])

# Once nyt_clean_up is done on all the files, we save it toa large text file
# that can be used as the import for pre-processing code. 
def write_to_file():
    nyt_final_text = '\n'.join(nyt_corpus)
    nyt_file = open("nytData.txt", "w")
    nyt_file.write(nyt_final_text)
    nyt_file.close()


nyt_corpus = []
nyt_ids = []

# For each file, we have to make sure it only contains nyt articles
# Load the json data from each file and parse it
# then send it for clean up 
for file in files_list:
    print(file)
    with open(file) as f_input:
        json_data = json.load(f_input)
        for article in json_data:
            if article['type'] == 'nyt':
                nyt_clean_up(article)
    print(len(nyt_ids))
write_to_file()
