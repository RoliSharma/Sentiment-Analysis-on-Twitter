from Datastore import df
from Feature_Extraction import vector
from new_training import vect
from new_training import dframe
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
print('hi ')

#for training dataset -->  (0 = negative, 2 = neutral, 4 = positive)

X_train,y_train=vect,dframe.sentiment
X_test = vector
y_test = df.sentiment
#X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=30)
clf = MultinomialNB().fit(X_train, y_train)
y_pred=clf.predict(X_test)
print(accuracy_score(y_test,y_pred))


p,n,nt=0,0,0
for i in y_pred:
    if i=="Positive":
        p=p+1;
    elif i=="Negative":
        n=n+1;
    else:
        nt=nt+1;
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Sentiment = ['Positive', 'Neutral', 'Negative']
NoT= [p,nt,n]
ax.bar(Sentiment,NoT)
plt.show()
