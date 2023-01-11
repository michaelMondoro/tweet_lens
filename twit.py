import pymongo
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


# Calculate sentiment
def calculate_sentiment(trend, cur_pos, cur_neg, cur_total):
    pos = cur_pos + trend.pos 
    neg = cur_neg + trend.neg 
    total = cur_total + trend.tweets 

    return ( round(pos/total*100,2), round(neg/total*100,2) )

'''
# Trend dictionary
{
    "name": trend_name,
    "volume": volume,
    "tweets": tweets,
    "reg_tweets": reg_tweets,
    "retweets": retweets,
    "positive_tweets": positive_tweets,
    "negative_tweets": negative_tweets,
    "sentiment": sentiment,
    "impact": impact,
    "top_users": [(user,num_tweets),(user,num_tweets)],
    "top_locations": [(location,num_tweets),(location,num_tweets)]
}

# increment db field by 1
trends.update_one({'field':value},{"$inc": {'field_to_increment':1}})
# update value to new value
trends.update_one({'field':value},{"$set": {'field':new_value}})

db.list_collection_names()


'''

def process():
    # Connect to mongoDB
    client = pymongo.MongoClient()
    db = client.tweet_lens_db
    trends = db.trends 

    # Get current list of trends in DB
    trend_list = [trend['name'] for trend in trends.find()]

    # Set up Twitter processing
    a = TwitAnalyzer()
    live = TwitLive(a)

    # Live trend processing
    live.TopTrendsAnalysis("Worldwide", 10, False)

    for trend in live.trend_streams:
        trend_document = {
            "name": trend.name, "volume": trend.volume,
            "tweets": trend.tweets, "reg_tweets": trend.reg_tweets,
            "retweets": trend.retweets, "positive_tweets": trend.pos,
            "negative_tweets": trend.neg, "sentiment": trend.get_sentiment(),
            "impact": trend.impact_raw, "top_users": [],
            "top_locations": []
        }

        # If trend exists, update the DB values
        if trend.name in trend_list:
            cur_trend = trends.find_one({"name":trend.name})
            sentiment = calculate_sentiment(trend, cur_trend["positive_tweets"], cur_trend["negative_tweets"], cur_trend["tweets"])
            trends.update_one({"name":trend.name},
                {
                "$inc": {  "tweets":trend.tweets, 
                            "reg_tweets": trend.reg_tweets,
                            "retweets": trend.retweets,
                            "positive_tweets": trend.pos,
                            "negative_tweets": trend.neg,
                            "impact": trend.impact_raw
                        },
                "$set": {   "sentiment":sentiment }
                })
        # If trend doesn't exist, add it to the DB
        else:
            trends.insert_one(trend_document)



        
