from sklearn.feature_extraction.text import CountVectorizer 
from preprocessing import tweets

# Create a vectorizer Object
vectorizer = CountVectorizer() 
  
vectorizer.fit(tweets) 
vector = vectorizer.transform(tweets).toarray()



