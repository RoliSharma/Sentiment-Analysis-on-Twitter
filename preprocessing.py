# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:20:49 2021

@author: HP
"""

from TweepyAPI_Extended import tweet_list
import preprocessor as p

dataset=[]

for tweet in tweet_list:    
    tweet=p.tokenize(tweet)
     
    
for tweet in tweet_list:
    p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.HASHTAG,p.OPT.RESERVED,p.OPT.NUMBER)
    dataset.append(p.clean(tweet))   
    
for tweet in dataset:
    tweet=tweet.lower()
    #remove punctuations
    words=tweet.split(" ")
    for i in words:
        if(len(i)<2):
            words.remove(i)
    print(words)
    print("---------------------------------------------------------")
    
    
