import tweepy
import codecs

#DONT FORGET TO CHANGE THESE TO YOUR OWN SECRETS AND TOKENS!!!!
access_token = ""
access_token_secret = ""
consumer_token = ""
consumer_secret = ""


#Listener to print incoming tweets from twitter.
class StreamListener(tweepy.StreamListener): 

	def on_status(self, status):

		print(status)

	def on_error(self, status):
		
		print status
		if status == 420:

			return False



if __name__ == '__main__':

	stream_listener = StreamListener()
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, stream_listener)


	stream.filter(track=['Bitcoin', 'Litecoin', 'Ethereum'])
	#stream.sample()