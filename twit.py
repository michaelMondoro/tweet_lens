import tweepy
import yaml
from termcolor import cprint, colored
from TwitStream import TwitStream
from TwitAnalyzer import TwitAnalyzer

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

total_tweets = 0
compute_time = 0 


'''
Utility Functions
'''
# Convert seconds to (mins,seconds)
def get_time(seconds):
    if seconds > 60:
        return (round(seconds/60),seconds%60)
    return (0,seconds)

# Function used to create and start a Twitter stream
def stream(analyzer, query):
    stream = TwitStream(analyzer.config['CONSUMER_KEY'],analyzer.config['CONSUMER_SECRET'],analyzer.config['ACCESS_TOKEN'],analyzer.config['ACCESS_TOKEN_SECRET'])
    print(f"FILTERING: {query}")
    stream.filter(track=[query])


if __name__ == "__main__":
    a = TwitAnalyzer()
    results = a.get_topic_data('black lives matter')