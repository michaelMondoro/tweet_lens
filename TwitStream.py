import tweepy
from termcolor import cprint, colored


'''
# Custom stream class for streaming live tweet data
'''
class TwitStream(tweepy.Stream):
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

    def on_error(self, status_code):
        print(status_code)


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