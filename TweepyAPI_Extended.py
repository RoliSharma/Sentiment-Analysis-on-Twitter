import tweepy
from gui import value

access_token="1306511356775010305-RW0inFN6dMQgYsaCNel5CcNtgO7aRT"
access_token_secret="R6KXPDe1qOjNj8yt0sup0jh80eTKkODi9hGvnIlSN9kWx"
consumer_key="Jafhqf236ZtyL3x2rvwuSn7pE"
consumer_secret="G4P7vp4mFUFJ66l4Jwh2BKOnFQnBrbISSyCV9RfiPkH8FhX93j"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

text_query = value()
count = 150
tweet_list=[]

# Creation of query method using parameters
tweets1 = tweepy.Cursor(api.search,q=text_query,truncated=False,lang="en",tweet_mode="extended",result_type="mixed",retweeted_status=True).items(count)

text_query = 'sad'


# Creation of query method using parameters
tweets2 = tweepy.Cursor(api.search,q=text_query,truncated=False,lang="en",tweet_mode="extended",result_type="mixed",retweeted_status=True).items(count)
         
#Pulling information from tweets iterable object
for tweet in tweets1 :
    try:
        tweet_list.append(tweet.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        tweet_list.append(tweet.full_text)        

for tweet in tweets2 :
    try:
        tweet_list.append(tweet.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        tweet_list.append(tweet.full_text)        

