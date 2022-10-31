import tweepy
import yaml
import redis
from TwitStream import TwitStream
from TwitAnalyzer import TwitAnalyzer
from TwitLive import TwitLive


'''
File for testing Twitter analysis tools
'''
# ------
# NOTES
# ------

# Search for tweets
# query_results = api.search_tweets(q="",tweet_mode="extended") # ONLY searches within past 7 days
# geo_results = api.search_geo(lat,lon,tweet_mode="extended")

# Twitter search operators
# https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators


# Time Formatting
#tweet.created_at.astimezone().strftime('%m/%d/%Y - %I:%M %p')


'''
Utility Functions
'''
# Convert seconds to (hours,mins,seconds)
def get_hrs_mins(seconds):
    hrs = round(seconds / 3600)
    mins = 0
    seconds = seconds % 3600
    if seconds >= 60:
        mins = int(seconds / 60)
        seconds = seconds % 60
    return (hrs,mins,seconds)



if __name__ == "__main__":
    a = TwitAnalyzer()
    live = TwitLive(a)
    live.trend_stats("Worldwide", 5, False)
    
    # Test redis
    # db = redis.Redis()
    # tweets = a.api.search_tweets("black lives matter",count=10)
    # for tweet in tweets:
    #     db.hset(f"tweet:{tweet.id}","text",tweet.text)
    #     db.hset(f"tweet:{tweet.id}","likes",tweet.favorite_count)
