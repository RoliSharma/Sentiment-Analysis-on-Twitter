from textblob import TextBlob
from preprocessing import tweets

sentiment=[]
label=[]

for tweet in tweets:
    total=0
    lab=""
    words=tweet.split(" ")
    for word in words:
        w = TextBlob(word)
        total+=w.sentiment.polarity
    if total<=-0.2:
        lab="Negative"
        flag=0
    elif total>-0.2 and total<0.2:
        lab="Neutral"
        flag=1
    else:
        lab="Positive"
        flag=2
    label.append(lab)
    sentiment.append(total)
    print(tweet,"-------",total)
    
    
