import tweepy
import yaml
from termcolor import cprint, colored
import time
import signal 


# ------
# NOTES
# ------
# Search for tweets
# query_results = api.search_tweets(q="",tweet_mode="extended") # ONLY searches within past 7 days
# geo_results = api.search_geo(lat,lon,tweet_mode="extended")
#tweet.created_at.astimezone().strftime('%m/%d/%Y - %I:%M %p')


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

    signal.signal(signal.SIGINT, stream.exit_gracefully)
    stream.filter(track=[query])



'''
# Custom stream class for streaming live tweet data
'''
class TwitStream(tweepy.Stream):
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        self.total_tweets = 0
        self.time = time.perf_counter()

        super().__init__(consumer_key,consumer_secret,access_token,access_token_secret)

    def print_tweet(self, tweet, text, quoted_text, url, quote_url):

        # Print header for tweet or retweet
        if hasattr(tweet, 'retweeted_status'):
            print(f"{colored(tweet.author.name,'cyan')} retweeted {colored(tweet.retweeted_status.author.name,'yellow')}")

        else:
            print(f"{colored(tweet.author.name,'cyan')} tweeted")

        # Print location if there
        if tweet.author.location:
            print(f"[{colored(tweet.author.location,'magenta')}] ---")
        else:
            print(f"[{colored('***','magenta')}] ---")


        # Print tweet contents
        print(f"[{colored(url,'red')}]")
        print(text)

        # Print quote if there
        if hasattr(tweet, 'quoted_status'):
            print(f"{colored(tweet.quoted_status.author.name,'yellow')}\n[{colored(quote_url,'red')}]\n{colored(quoted_text,'blue')}")

        print("---\n\n")


    # Get the url associated with the given tweet
    def get_url(self, status):
        if len(status.entities['urls']) > 0:
            return status.entities['urls'][0]['url']
        else:
            return ""

    # Get text associated with the given tweet
    def get_text(self, status):
        if hasattr(status, 'extended_tweet'):
            return status.extended_tweet['full_text']
        else:
            return status.text

    def exit_gracefully(self, signum, frame):
        input("EXIT??? ")
        self.time = time.perf_counter() - self.time

        print(f"[ Processed: {stream.total_tweets} in {get_time(stream.time)} ]")

    def on_status(self, status):
        if exit:
            return False
        retweet_text = ""
        retweet_url = ""
        quoted_text = ""
        quote_url = ""

        # Get text from retweet
        if hasattr(status, 'retweeted_status'):
            retweet_url = self.get_url(status.retweeted_status)
            retweet_text = self.get_text(status.retweeted_status)

        # Get text from quoted tweet
        if hasattr(status, 'quoted_status'):
            quote_url = self.get_url(status.quoted_status)
            quoted_text = self.get_text(status.quoted_status)

        # Get text from tweet
        url = self.get_url(status)
        text = self.get_text(status)

        if hasattr(status, 'retweeted_status'):
            self.print_tweet(status, retweet_text, quoted_text, retweet_url, quote_url)
        else:
            self.print_tweet(status, text, quoted_text, url, quote_url)

        self.total_tweets += 1



'''
# Class for processing and analyzing Tweets
'''
class TwitAnalyzer:
    def __init__(self):
        self.config = None
        self.api = self.init_twitter()

    def sample_size(self, pop, z, err,):
        numerator = (z**2 * .25) / err**2
        denominator = 1 + (z**2 * .25) / (err**2 * pop)
        return round(numerator/denominator,2)


    def init_twitter(self):
        with open('.config') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

        # Initialize twitter connection
        auth = tweepy.OAuthHandler(self.config['CONSUMER_KEY'],self.config['CONSUMER_SECRET'])
        auth.set_access_token(self.config['ACCESS_TOKEN'],self.config['ACCESS_TOKEN_SECRET'])
         
        api = tweepy.API(auth,wait_on_rate_limit=True)
        return api 

    def get_trend_locations(self):
        trend_locations = {}
        trends = self.api.available_trends()

        for trend in trends:
            trend_locations[trend['name']] = {'woeid': trend['woeid'], 'parent': trend['parentid']}

        return trend_locations


if __name__ == "__main__":
    a = TwitAnalyzer()
    stream(a, "green bay packers")