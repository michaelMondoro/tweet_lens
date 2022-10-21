import tweepy
import yaml
from time import sleep
from termcolor import cprint, colored
from TwitStream import TwitStream
from TwitAnalyzer import TwitAnalyzer
from progress.spinner import *
from prettytable import *

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

# Function used to create and start a Twitter stream
def stream(analyzer, query, live):
    stream = TwitStream(analyzer.config['CONSUMER_KEY'],analyzer.config['CONSUMER_SECRET'],analyzer.config['ACCESS_TOKEN'],analyzer.config['ACCESS_TOKEN_SECRET'], live=live)
    thread = stream.filter(track=[query], stall_warnings=True, threaded=True)
    return stream, thread

# Display progress spinner for certain amount of seconds
def progress(text, secs):
    spin = PixelSpinner(text)
    for i in range(secs*4):
        spin.next()
        sleep(.25)
    spin.finish()

def trend_stats(location, num_trends, live):
    trends = a.get_trends(a.trend_locations[location]["woeid"])
    data={}
    total_tweets = 0
    total_retweets = 0
    total_unique_retweets = 0
    total_volume = 0

    if num_trends == 'all':
        num_trends = len(trends)

    print(f"Gathering data on top {num_trends} trends from [ {location} ]")
    for i, trend in enumerate(trends[:num_trends]):
        # Start stream and print status
        streem, thread = stream(a, trend['name'], live)
        if not live:
            progress(f" {i+1}/{num_trends} [ {colored(trend['name'],'magenta')} ] - Volume: {trend['tweet_volume']:,} ", 30)
        else:
            print(f" {i+1}/{num_trends} [ {trend['name']} ] - Volume: {trend['tweet_volume']:,}")
            sleep(30)
        

        # Disconnect stream and wait for thread to finish
        streem.disconnect()
        thread.join()

        total_tweets += streem.num_tweets
        total_retweets += streem.num_retweets
        total_unique_retweets += streem.get_unique_retweets()
        total_volume += trend['tweet_volume']
        
        data[trend['name']] = { 'tweets':streem.num_tweets,
                                'retweets':streem.num_retweets, 
                                'unique_retweets':streem.get_unique_retweets(),
                                'tw_p_min': streem.num_tweets*2}


    # Create results table
    table = PrettyTable(['Trend', 'Tweets', 'Retweets', 'Unique Retweets', 'twt/min', '% Retweets', '% Unique Retweets'])
    table.set_style(SINGLE_BORDER)
    table.align = 'l'

    for trend in data:
        perc_retweet = 0
        if data[trend]['tweets'] > 0:
            perc_retweet = round((data[trend]['retweets']/data[trend]['tweets'])*100,2)
        table.add_row([trend, data[trend]['tweets'], data[trend]['retweets'], data[trend]['unique_retweets'], data[trend]['tw_p_min'], perc_retweet, round((data[trend]['unique_retweets']/data[trend]['retweets'])*100,2)])
    table.add_row(['Summary', total_tweets, total_retweets, total_unique_retweets, round(total_tweets/(num_trends/2)), round((total_retweets/total_tweets)*100,2), round((total_unique_retweets/total_retweets)* 100,2)])    

    print(table)
    print(f"\nProcessed {round((total_tweets/total_volume)*100,4)}% of total volume")
    print(f"[{total_tweets-total_retweets} regular ] [ {total_retweets} retweets ] [ {total_unique_retweets} unique retweets ]")
    print("\n\n")

if __name__ == "__main__":
    a = TwitAnalyzer()

    trend_stats("United States", 3, False)
    
