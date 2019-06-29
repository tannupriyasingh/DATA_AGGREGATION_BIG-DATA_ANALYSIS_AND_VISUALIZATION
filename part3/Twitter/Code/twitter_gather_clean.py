#!/usr/bin/env python

import glob
import os
import json
import re
import emoji

# We have to do some basic clean up here as tweets contain things that other
# data source might not. Therefore, we remove "@" and "#" and also make sure no urls are there.
# In addition we have to make sure to remove all emojis.
# we also make sure that no tweet is repeated across all the tweet base and including
# that the exact was not copied and retweeted to aovid the retweets status.
def twitter_clean_up(article):
    if not article['id'] in tweet_ids and not article['full_text'] in twitter_corpus:
        article['full_text'] = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', article['full_text'], flags=re.MULTILINE)
        article['full_text'] = re.sub(r'([@#]+)', '', article['full_text'], flags=re.MULTILINE)
        article['full_text'] = article['full_text'].replace("&amp;", "")
        article['full_text'] = article['full_text'].replace("&lt;", "")
        article['full_text'] = emoji.get_emoji_regexp().sub(r'', article['full_text'])
        twitter_corpus.append(article['full_text'])
        tweet_ids.append(article['id'])

# After everything is done, we save the tweets in once big file for pre-processing
def write_to_file():
    twitter_final_text = '\n'.join(twitter_corpus)
    twitter_file = open("twitterData_test.txt", "w")
    twitter_file.write(twitter_final_text)
    twitter_file.close()

# Import all the files required.
files_list = glob.glob(os.path.join(os.getcwd(), "../twitter_raw_data/tweets_json_*.txt"))

twitter_corpus = []
tweet_ids = []

# For each file, it will clean up and give us the count of tweets it successfully got it from it. 
for file in files_list:
    print(file)
    with open(file) as f_input:
        json_data = json.load(f_input)
        for article in json_data:
            if article['type'] == 'twitter':
                twitter_clean_up(article)
    print(len(tweet_ids))
write_to_file()
