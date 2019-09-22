import tweepy
import codecs
import sys
import time
import json
import boto3
import datetime
#python script in aws lambda > batch data in S3 > Batch data into aws emr > final result into S3 or redshift

#in your twitter_keys.txt file, make sure you have the access token on first line, then access_token_secret on second line, then consumer_token on third line, and consumer_secret on fourth line in txt file.
#with open("twitter_keys.txt") as key_file:
with open("twitter_keys.txt") as key_file:
	data = key_file.readlines()
data = [x.strip() for x in data]

access_token = str(data[0])
access_token_secret = str(data[1])
consumer_token = str(data[2])
consumer_secret = str(data[3])


#this is for AWS access key and secret key to store json file output in AWS S3
with open("rootkey.csv") as aws_key_file:
    data_aws_key_file = aws_key_file.readlines()
aws_access_key = str(data_aws_key_file[0]).strip()
aws_secret_key = str(data_aws_key_file[1]).strip()

aws_access_key = aws_access_key[15:]
aws_secret_key = aws_secret_key[13:]
#twitter serves only tweets for the past week, so i need to automate and run this every week for multiple weeks and dump the outputl file in S3 to be used all together.



MAX_TWEETS = 1000
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

counter = 0

outputfile = 'batchtest' + str(datetime.date.today()) + '.json'
#2591 Rate limit reached. Sleeping for: 723
api = tweepy.API(auth,wait_on_rate_limit = False, wait_on_rate_limit_notify = True)
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
    with open(outputfile, 'a') as my_json:
		#json.dump(tweet_text, my_json)
        #json.dump(tweet_text, my_json)
        json.dump(tweet_json, my_json)
        my_json.write('\n')    


#This is for uploading the new recent json file to our S3 bucket.
s3 = boto3.client('s3', aws_access_key_id=aws_access_key,aws_secret_access_key=aws_secret_key)
s3.upload_file(outputfile, 'ryanztwitters3bucket', outputfile)
