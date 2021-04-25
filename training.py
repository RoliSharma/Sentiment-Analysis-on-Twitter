
#from Datastore import df
#from Feature_Extraction import vector
#from new_training import vect
#from new_training import dframe
#from sklearn.model_selection import train_test_split
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import accuracy_score

import nltk
import matplotlib.pyplot as plt
from sentiment import preprocessed_test_set
from Feature_Extraction import training_features
from Feature_Extraction import extract_features

NBayesClassifier = nltk.NaiveBayesClassifier.train(training_features)
NBResultLabels = [NBayesClassifier.classify(extract_features(tweet[0])) for tweet in preprocessed_test_set]
print(NBResultLabels)

#for training dataset -->  (0 = negative, 2 = neutral, 4 = positive)

#X_train,y_train=vect,dframe.sentiment
#type of X_train = <class 'numpy.ndarray'>
#print(f"type of X_train = {type(X_train)}")
#X_test = vector
#y_test = df.sentiment
#X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=30)
#clf = MultinomialNB().fit(X_train, y_train)
#y_pred = clf.predict(X_test)
#print(accuracy_score(y_test, y_pred))

p,n,nt = 0,0,0

for i in NBResultLabels:
    if i=='3':
        nt=nt+1;
    elif i=='1':
        n=n+1;
    elif i=='5':
        p=p+1;

Sentiment_label = ['Positive','Neutral','Negative']
NoT= [p,nt,n]
print(f'positive = {p}')
print(f'negative = {n}')
print(f'neutral = {nt}')

