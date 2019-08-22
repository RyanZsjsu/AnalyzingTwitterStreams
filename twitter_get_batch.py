import tweepy
import codecs
import sys
import time
import json


#in your twitter_keys.txt file, make sure you have the access token on first line, then access_token_secret on second line, then consumer_token on third line, and consumer_secret on fourth line in txt file.
#with open("twitter_keys.txt") as key_file:
with open("twitter_keys.txt") as key_file:
	data = key_file.readlines()
data = [x.strip() for x in data]

access_token = str(data[0])
access_token_secret = str(data[1])
consumer_token = str(data[2])
consumer_secret = str(data[3])

#twitter serves only tweets for the past week, so i need to automate and run this every week for multiple weeks and dump the outputl file in S3 to be used all together.
#output_file = 'batchtest1.txt'
MAX_TWEETS = 5000
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

counter = 0
#2591 Rate limit reached. Sleeping for: 723
api = tweepy.API(auth,wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
for tweet in tweepy.Cursor(api.search, q='Trump OR DonaldTrump OR Donald Trump', tweet_mode = 'extended', rpp=100).items(MAX_TWEETS):
    print('Loop')
    
    print(counter)
    counter = counter + 1
    if 'extended_tweet' in tweet._json: 
        tweet_json = tweet._json['extended_tweet']['full_text'] 
        print('extended_tweet case')
    elif 'retweeted_status' in tweet._json and 'extended_tweet' in tweet._json['retweeted_status']: 
        tweet_json = tweet._json['retweeted_status']['extended_tweet']['full_text'] 
        print('retweeted_status and extended_tweet case')
    elif 'retweeted_status' in tweet._json: 
        tweet_json = tweet._json['retweeted_status']['full_text'] 
        print('retweeted_status case')
    else: 
        tweet_json = tweet._json['full_text']
        print('full text case') 
    #print(tweet_json)

    
    #tweet2 = tweet._json
    #tweet_text = tweet2.get("full_text", {})
    with open('batchtest.json', 'a') as my_json:
		#json.dump(tweet_text, my_json)
        #json.dump(tweet_text, my_json)
        json.dump(tweet_json, my_json)
        my_json.write('\n')    




 
