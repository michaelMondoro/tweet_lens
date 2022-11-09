from TwitAnalyzer import TwitAnalyzer
from TwitStream import TwitStream
import redis

'''
Module for processing twitter data offline
'''
class TwitProcess:
    self.analyzer = TwitAnalyzer()
    self.db = redis.Redis()
    

    # Get current data for topic
    def get_data(self, topic):
        return db.hgetall(f"topic:{topic}")

    # Process bulk twitter data related to specified query
    def BulkAnalysis(self, query):
        tweets = analyzer.api.search_tweets(query,count=100)
        for tweet in tweets:

            # TODO: Sentiment Processing 

            # TODO: Save query data to db
            # db.hset(f"topic:{query}","tweets",tweet.text)
            # db.hset(f"topic:{query}","likes",tweet.favorite_count)
            # db.expire(f"topic:{query}", TIMEOUT)
