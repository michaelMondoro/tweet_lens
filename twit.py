import tweepy
import yaml


# Search for tweets
# query_results = api.search_tweets(q="",tweet_mode="extended") # ONLY searches within past 7 days
# geo_results = api.search_geo(lat,lon,tweet_mode="extended")



class TwitAnalyzer:

	def __init__(self):
		self.api = None

		self.init_twitter()


	def sample_size(self, pop, z, err,):
		numerator = (z**2 * .25) / err**2
		denominator = 1 + (z**2 * .25) / (err**2 * pop)
		return round(numerator/denominator,2)


	def init_twitter(self):
		with open('.config') as file:
			config = yaml.load(file, Loader=yaml.FullLoader)

		# Initialize twitter connection
		auth = tweepy.OAuthHandler(config['CONSUMER_KEY'],config['CONSUMER_SECRET'])
		auth.set_access_token(config['ACCESS_TOKEN'],config['ACCESS_TOKEN_SECRET'])
		 
		self.api = tweepy.API(auth,wait_on_rate_limit=True)
		

	def get_trend_locations(self):
		trend_locations = {}
		trends = self.api.available_trends()

		for trend in trends:
			trend_locations[trend['name']] = {'woeid': trend['woeid'], 'parent': trend['parentid']}

		return trend_locations




# results = []
# max_id = 0
# while len(results) < 300:
# 	q = api.search_tweets(q="Kyle Pitts",tweet_mode="extended",count=100,max_id=max_id)
# 	results += list(q)
# 	max_id = q.max_id
# 	print(len(results))
