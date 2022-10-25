from TwitAnalyzer import TwitAnalyzer
from TwitStream import TwitStream

'''
Module for processing live twitter data
'''
class Live:
	a = TwitAnalyzer()

	# Create and start a Twitter stream
	def stream(query, live):
	    twit_stream = TwitStream(a.config['CONSUMER_KEY'],a.config['CONSUMER_SECRET'],a.config['ACCESS_TOKEN'],a.config['ACCESS_TOKEN_SECRET'], live=live)
	    thread = twit_stream.filter(track=[query], stall_warnings=True, threaded=True)
		return twit_stream, thread

	# Process live twitter trend data
	def TrendAnalysis(self):
		pass

	# Process live twitter search data
	def SearchAnalysis(self):
		pass
