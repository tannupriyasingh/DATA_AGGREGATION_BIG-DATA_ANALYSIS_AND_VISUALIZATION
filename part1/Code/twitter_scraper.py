# -*- coding: utf-8 -*-

import tweepy
import datetime
import json

# Insert your API details from Twitter here
consumer_key = "XXXXX"
consumer_secret = "XXXXX"
access_token = "XXXXX"
access_token_secret = "XXXXX"

# Setup the pakcage tweepy to use the Auth details and create a connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# The input date format to be modified during storage
input_time_format = '%a %b %d %H:%M:%S %z %Y'
# The output date format to be modified and stored in the output file.
output_time_format = '%Y-%m-%dT%H:%M:%S'
# List to store the tweets
tweets_list = []
# Just a list of IDs to make sure we do not retrieve the article within the same search
tweets_ids = []
# Total number of tweets collected in the specific search
total_tweets: int = 0
# The query to search against
query: str = 'planned parenthood -filter:retweets'
# How many tweets we want.
count_per_search: int = 1000
# The search happens here where it takes all the params and runs the full search.
# Cursor helps in keeping the connection alive when we hit an API limit and
search_results = tweepy.Cursor(api.search, q=query, lang="en", tweet_mode="extended", result_type="recent").items(count_per_search)

# We will now go over each tweet object and if it is not retweeted then
# we will save the required parts of it and push it to a list
for status in search_results:
    tweet: object = status._json
    if not tweet['retweeted']:
        clean_tweet: object = {
            'type': 'twitter',
            'full_text': tweet['full_text'],
            'id': tweet['id'],
            'created_at': datetime.datetime.strptime(tweet['created_at'], input_time_format).strftime(output_time_format),
            'lang': tweet['lang'],
            'retweeted': tweet['retweeted']
        }

        if not clean_tweet['id'] in tweets_ids:
            tweets_list.append(clean_tweet)
            total_tweets += 1
            print(total_tweets)

# After going through the entire search results, we will save it to file.
with open("tweets_json_planned_parenthood_1000.txt", "w") as open_file:
    json.dump(tweets_list, open_file, ensure_ascii=False)
