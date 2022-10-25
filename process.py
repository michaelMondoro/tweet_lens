from TwitAnalyzer import TwitAnalyzer
import redis

'''
Module for processing bulk twitter data
'''

class Process:
	a = TwitAnalyzer()
	db = redis.Redis()

	def BulkAnalysis(query):
	    tweets = a.api.search_tweets(query,count=10)
	    for tweet in tweets:

	    	# TODO: Sentiment Processing 

	    	# TODO: Save tweet data to db
	        db.hset(f"tweet:{tweet.id}","text",tweet.text)
	        db.hset(f"tweet:{tweet.id}","likes",tweet.favorite_count)
		