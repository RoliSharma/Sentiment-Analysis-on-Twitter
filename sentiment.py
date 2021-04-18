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
        lab=1
        flag=0
    elif total>-0.2 and total<0.2:
        lab=3
        flag=1
    else:
        lab=5
        flag=2
    label.append(lab)
    sentiment.append(total)
    print(tweet,"-------",total)
    
    
