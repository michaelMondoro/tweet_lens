# tweet_lens
[![Generic badge](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-yes-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-3.10.6-yellow.svg)](https://shields.io/)

Project for extrapolating the sentiment, impressions and impact of different topics trending on Twitter.

## Functionality
Project is split into two main modules. The `TwitLive` module is used for streaming/processing live Twitter data. The `TwitProcess` module is used for processing bulk Twitter data.

Example use of `TwitLive`
```python
from TwitLive import TwitLive

# Make sure to have your keys/tokens defined in your '.config' file. See example file for details
live = TwitLive(a)
live.TrendAnalysis("United States", 3, False)

```

![tweets](https://user-images.githubusercontent.com/38412172/197245058-916f99d9-5c0d-437d-80e3-158a8e3af039.png)


TODO:
  - [ ] Implement Redis backend to store trend / search data
  - [ ] Implement bulk analysis processing
  - [x] Implement live stream functionality
  - [ ] Results dashboard (design, UI, Flask framework)
  - [ ] Analysis of twitter topic/trend in relation to an individual user
  - [ ] Implement `Impact` and `Reach` analysis
  
  
