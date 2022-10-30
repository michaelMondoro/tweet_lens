from TwitAnalyzer import TwitAnalyzer
from TwitStream import TwitStream

'''
Module for processing live twitter data
'''
class TwitLive:
	analyzer = TwitAnalyzer()

	# Create and start a Twitter stream
	def stream(self, query, live):
	    twit_stream = TwitStream(analyzer.config['CONSUMER_KEY'],analyzer.config['CONSUMER_SECRET'],analyzer.config['ACCESS_TOKEN'],analyzer.config['ACCESS_TOKEN_SECRET'], live=live)
	    thread = twit_stream.filter(track=[query], stall_warnings=True, threaded=True)
		return twit_stream, thread

	# Process live twitter trend data
	def TrendAnalysis(self):
		pass

	# Process live twitter search data
	def SearchAnalysis(self):
		pass
