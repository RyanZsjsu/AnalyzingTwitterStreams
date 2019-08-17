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


output_file = 'streamtest1.txt'


#Listener to print incoming tweets from twitter.
#class StreamListener(tweepy.StreamListener): 

#	def on_status(self, status):
	#	with open(output_file, 'w', encoding = "utf-8") as outfile:
		#	outfile.write(str(status))
		


	#def on_error(self, status):
		
		#print(status)
		#if status == 420:

			#return False


class listener(tweepy.StreamListener):
	def on_data(self, data):
		try:
			tweet = json.loads(data)
			tweet_text = tweet.get("text", {})
			with open('streamtest.json', 'a') as my_json:
				#json.dump(tweet, my_json)
				json.dump(tweet_text, my_json)
		except BaseException:
			print('Error')
			pass

	def on_error(self, status):
		print(statuses)

if __name__ == '__main__':

	#stream_listener = StreamListener()
	#auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	#auth.set_access_token(access_token, access_token_secret)
	#stream = tweepy.Stream(auth, stream_listener)
	#stream.filter(track=['Bitcoin', 'Litecoin', 'Ethereum'])

	my_listenser = listener()
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, my_listenser)
	#stream.filter(track=['Bitcoin', 'Litecoin', 'Ethereum'])
	stream.filter(track=['Trump', 'DonaldTrump', 'Donald Trump', 'President Trump'])
	
