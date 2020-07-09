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

# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets if keyword in tweet.text]

# Printing tweet data containing keyword
tweets_df = pd.DataFrame(text_tweets, columns = ['Datetime', 'Text']) 

# Converting tweets dataframe to csv file
tweets_df.to_csv('{}-{}-tweets.csv'.format(username, keyword), sep='|')
