#!/usr/bin/python3

# A simple Tweet scrapper to extract all tweets containing a keyword for a certain username
# Author: Jay Shah
# Date: Jul 8, 2020

import GetOldTweets3 as got
import pandas as pd
import sys

username = str(sys.argv[1])
count = int(sys.argv[2])
keyword = str(sys.argv[3])

# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(count)

# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# Printing tweet data containing keyword
for tweet in tweets:
    if keyword in tweet.text:
        print (tweet.date, tweet.text)
