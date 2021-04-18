# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:20:28 2021

@author: HP
"""
import numpy as np
import pandas as pd
from preprocessing import tweets
from sentiment import sentiment,label
from sklearn.feature_extraction.text import TfidfVectorizer
df=pd.DataFrame({"value":sentiment,"sentiment":label,"tweet":tweets})
print(df)
#df.to_csv('dataset.csv') 
#print(df.head())


#print(len(tweets),"_",len(sentiment),"_",len(label))



