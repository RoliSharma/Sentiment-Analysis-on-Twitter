# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:22:33 2021

@author: HP
"""

import tweepy

access_token="1306511356775010305-RW0inFN6dMQgYsaCNel5CcNtgO7aRT"
access_token_secret="R6KXPDe1qOjNj8yt0sup0jh80eTKkODi9hGvnIlSN9kWx"
consumer_key="Jafhqf236ZtyL3x2rvwuSn7pE"
consumer_secret="G4P7vp4mFUFJ66l4Jwh2BKOnFQnBrbISSyCV9RfiPkH8FhX93j"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

text_query = 'Python'
count = 150
tweet_list=[]

# Creation of query method using parameters
tweets = tweepy.Cursor(api.search,q=text_query,truncated=False,lang="en",tweet_mode="extended",result_type="mixed",retweeted_status=True).items(count)
 
            
#Pulling information from tweets iterable object
for tweet in tweets:
    try:
        tweet_list.append(tweet.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        tweet_list.append(tweet.full_text)        
