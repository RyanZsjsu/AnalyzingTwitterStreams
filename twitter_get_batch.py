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
    #tweet2 = json.loads(tweet._json)
    tweet2 = tweet._json
    tweet_text = tweet2.get("full_text", {})
    with open('batchtest.json', 'a') as my_json:
		#json.dump(tweet_text, my_json)
        json.dump(tweet_text, my_json)
        my_json.write('\n')    


# First you get the tweets in a json object
results = [status._json for status in tweepy.Cursor(api.search, q='Trump OR DonaldTrump OR Donald Trump', tweet_mode='extended', rpp=100).items()]
# Now you can iterate over 'results' and store the complete message from each tweet.
    

    my_tweets = []
    for result in results:
        my_tweets.append(result["full_text"])
        result["retweeted_status"]["full_text"]

    print(result[1][1])