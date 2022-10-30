# tweet_lens
[![Generic badge](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-yes-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-3.10.6-yellow.svg)](https://shields.io/)

Project for extrapolating the sentiment, impressions and impact of different topics trending on Twitter

## Functionality
Currently live twitter data based on a search term can be streamed and output to the console.
```python
from TwitLive import TwitLive

# Make sure to have your keys/tokens defined in your '.config' file. See example file for details
live = TwitLive(a)
live.trend_stats("United States", 3, False)

```

---
[ Example Run of `twit.py` ]

![tweets](https://user-images.githubusercontent.com/38412172/197245058-916f99d9-5c0d-437d-80e3-158a8e3af039.png)


TODO:
  - [ ] Implement backend to store tweet data
  - [ ] Automated scraping of tweets for bulk/historical analysis
  - [ ] Incorporation of live data with data from bulk analysis
  - [ ] Results dashboard
  - [ ] Analysis of twitter topic/trend in relation to an individual user
  
  
