# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:20:49 2021

@author: HP
"""

from TweepyAPI import dataset
import preprocessor as p


for i in dataset:
    print(p.tokenize(i["text"]))
   

for i in dataset:
    p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.HASHTAG,p.OPT.RESERVED,p.OPT.NUMBER)
    i["text"]=p.clean(i["text"])
    print(i["text"])
    print("-------------")
    
    

