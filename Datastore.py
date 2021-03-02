# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:20:28 2021

@author: HP
"""

import pandas as pd
from preprocessing import tweet_list

df=pd.DataFrame(tweet_list)
print(df)