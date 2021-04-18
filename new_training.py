import nltk
print('hi 2')
import pandas as pd
print('hi 4')
import preprocessor as p
print('hi 6')
from nltk.corpus import stopwords
print('hi 8')
#nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
print('hi 11')
from sklearn.feature_extraction.text import CountVectorizer
print('hi 13')
from preprocessing import tweets
print('hi 15')

#(0 = negative, 2 = neutral, 4 = positive)

porter = PorterStemmer()

dframe = pd.read_csv(r'C:\Project\Apple-Twitter-Sentiment-DFE.csv', nrows=100)
print(dframe.shape)

indexNames = dframe[dframe['sentiment'] == 'not_relevant'].index
dframe.drop(indexNames, inplace=True)

print('dframe')
print(dframe[0:5])

stop_words_list = set(stopwords.words('english'))
print(stop_words_list)

tweets_for_training = dframe[['sentiment','text']]
print(tweets_for_training.head(5))

training_tweets = dframe['text'].tolist()
sentiment_of_tweets = dframe['sentiment'].tolist()

cleaned_tweets = []
preprocessed_tweets = []

for t in training_tweets:
    t=p.tokenize(t)

for t in training_tweets:
    p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.HASHTAG,p.OPT.RESERVED,p.OPT.NUMBER,p.OPT.EMOJI)
    cleaned_tweets.append(p.clean(t))

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for t in cleaned_tweets:
    t=t.lower()
    # Removing punctuations in string, Using loop + punctuation string
    for element in t:
        if element in punc:
            t = t.replace(element,"")
    words_list=t.split(" ")
    filtered_sentence = ""
    for w in words_list:
        w=porter.stem(w)
        if w not in stop_words_list and len(w)>1:
            filtered_sentence+=w
            filtered_sentence+=" "
    preprocessed_tweets.append(filtered_sentence)

print(preprocessed_tweets[0:5])

# Create a vectorizer Object
vectorizer_obj = CountVectorizer()

vectorizer_obj.fit(preprocessed_tweets)
vect = vectorizer_obj.transform(preprocessed_tweets).toarray()







