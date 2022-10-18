import tweepy
import yaml

with open('.config') as file:
	config = yaml.load(file, Loader=yaml.FullLoader)


# results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
auth = tweepy.OAuthHandler(config['CONSUMER_KEY'],config['CONSUMER_SECRET'])
auth.set_access_token(config['ACCESS_TOKEN'],config['ACCESS_TOKEN_SECRET'])
 
api = tweepy.API(auth,wait_on_rate_limit=True)

'''
# Get locations for checking trends
list_of_available_trend_locations = api.available_trends()

# Get trend for location
# trends contain tweet_volume
us_trends = api.get_place_trend(us_woeid)



# Search for tweets
query_results = api.search_tweets(q="",tweet_mode="extended") # ONLY searches within past 7 days

geo_results = api.search_geo(lat,lon,tweet_mode="extended")


results = []
max_id = 0
while len(results) < 300:
	q = api.search_tweets(q="Kyle Pitts",tweet_mode="extended",count=100,max_id=max_id)
	results += list(q)
	max_id = q.max_id
	print(len(results))


'''
