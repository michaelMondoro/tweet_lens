# tweet_lens
[![Generic badge](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-yes-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-3.10.6-yellow.svg)](https://shields.io/)

Project for extrapolating the sentiment, impressions and impact of different topics trending on Twitter

## Functionality
Currently live twitter data based on a search term can be streamed and output to the console.
```python
from TwitAnalyzer import TwitAnalyzer
from TwitStream import TwitStream

# Make sure to have your keys/tokens defined in your '.config' file. See example file for details
a = TwitAnalyzer()
stream = TwitStream(a.config['CONSUMER_KEY'],a.config['CONSUMER_SECRET'],a.config['ACCESS_TOKEN'],a.config['ACCESS_TOKEN_SECRET'])
stream.filter(track=["your search to track"])

```

---
[ Example Run of `twit.py` ]

![tweets](https://user-images.githubusercontent.com/38412172/197244851-9ce9f890-1d9f-4da7-9123-a58193d612cf.png)


TODO:
  - [ ] Implement backend to store tweet data
  - [ ] Automated scraping of tweets for bulk/historical analysis
  - [ ] Incorporation of live data with data from bulk analysis
  - [ ] Results dashboard
  - [ ] Analysis of twitter topic/trend in relation to an individual user
  
  
