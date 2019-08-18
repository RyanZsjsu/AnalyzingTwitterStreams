import tweepy
import codecs
import sys
import time
import json


#in your twitter_keys.txt file, make sure you have the access token on first line, then access_token_secret on second line, then consumer_token on third line, and consumer_secret on fourth line in txt file.
with open("twitter_keys.txt") as key_file:
	data = key_file.readlines()
data = [x.strip() for x in data]

access_token = str(data[0])
access_token_secret = str(data[1])
consumer_token = str(data[2])
consumer_secret = str(data[3])


output_file = 'batchtest1.txt'
MAX_TWEETS = 5000000000000000000000
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
for tweet in tweepy.Cursor(api.search, q='Trump OR DonaldTrump OR Donald Trump', rpp=100).items(MAX_TWEETS):
    # Do something
    pass