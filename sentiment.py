from textblob import TextBlob
from new_preprocessing import preprocessed_test_tweets

sentiment_score = []
sentiment = []
preprocessed_test_set = []

for tweet in preprocessed_test_tweets:
    total=0
    lab=""
    for word in tweet:
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
    sentiment.append(lab)
    sentiment_score.append(total)
    preprocessed_test_set.append((tweet,lab))
    print(tweet,"-------",total)
    
    
