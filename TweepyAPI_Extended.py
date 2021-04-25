import tweepy
from gui import entry

access_token="1306511356775010305-RW0inFN6dMQgYsaCNel5CcNtgO7aRT"
access_token_secret="R6KXPDe1qOjNj8yt0sup0jh80eTKkODi9hGvnIlSN9kWx"
consumer_key="Jafhqf236ZtyL3x2rvwuSn7pE"
consumer_secret="G4P7vp4mFUFJ66l4Jwh2BKOnFQnBrbISSyCV9RfiPkH8FhX93j"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

text_query = entry
count = 150
test_tweet_list=[]

# Creation of query method using parameters
tweets1 = tweepy.Cursor(api.search,q=text_query,truncated=False,lang="en",tweet_mode="extended",result_type="mixed",retweeted_status=True).items(count)

for each_tweet in tweets1 :
    try:
        test_tweet_list.append(each_tweet.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        test_tweet_list.append(each_tweet.full_text)

