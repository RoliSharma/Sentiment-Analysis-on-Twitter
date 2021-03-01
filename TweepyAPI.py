import tweepy
import json

access_token="1306511356775010305-RW0inFN6dMQgYsaCNel5CcNtgO7aRT"
access_token_secret="R6KXPDe1qOjNj8yt0sup0jh80eTKkODi9hGvnIlSN9kWx"
consumer_key="Jafhqf236ZtyL3x2rvwuSn7pE"
consumer_secret="G4P7vp4mFUFJ66l4Jwh2BKOnFQnBrbISSyCV9RfiPkH8FhX93j"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_results = api.search(q="farmers", count=200)

dataset = [] 


#to view dataset in json format(readable)
#for i in search_results:
#    dataset.append(json.dumps(i._json, indent=4))
    
#for i in dataset:
#    print(i)
#    print("--------------------")
    

for i in search_results:
    if(i._json["retweet_count"]==0 and i._json["retweeted"]==False):
       # print(i)
        dataset.append(i._json)
    
    
#dataset is of data type dictionary
    
for i in dataset:
    print(i["text"])
    print("--------------------")