from sklearn.feature_extraction.text import CountVectorizer 
from preprocessing import tweets

# Create a Vectorizer Object 
vectorizer = CountVectorizer() 
  
vectorizer.fit(tweets) 
vector = vectorizer.transform(tweets).toarray()

