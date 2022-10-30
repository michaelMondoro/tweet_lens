from TwitAnalyzer import TwitAnalyzer
from TwitStream import TwitStream
import redis

'''
Module for processing live twitter data
'''
class TwitProcess:
    analyzer = TwitAnalyzer()

    # Process bulk twitter data related to specified query
    def BulkAnalysis(self, query):
        tweets = analyzer.api.search_tweets(query,count=10)
        for tweet in tweets:

            # TODO: Sentiment Processing 

            # TODO: Save tweet data to db
            # db.hset(f"tweet:{tweet.id}","text",tweet.text)
            # db.hset(f"tweet:{tweet.id}","likes",tweet.favorite_count)
            # db.expire(tweet.id, TIMEOUT)
