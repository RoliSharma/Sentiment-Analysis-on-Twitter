import nltk
import pandas as pd
#import preprocessor as p
#from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
#from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import tweets
from new_preprocessing import PreProcessTweets

#(0 = negative, 2 = neutral, 4 = positive)

porter = PorterStemmer()

dframe = pd.read_csv(r'C:\Project\Apple-Twitter-Sentiment-DFE.csv', nrows=100)
print(dframe.shape)

indexNames = dframe[dframe['sentiment'] == 'not_relevant'].index
dframe.drop(indexNames, inplace=True)

print('dframe')
print(dframe[0:5])

#stop_words_list = set(stopwords.words('english'))
#print(stop_words_list)

tweets_for_training = dframe[['sentiment','text']]
print(tweets_for_training.head(5))

training_tweets = dframe['text'].tolist()
sentiment_of_tweets = dframe['sentiment'].tolist()

preprocessedTrainingSet = []
tweetProcessor = PreProcessTweets()
preprocessedTrainingSet = tweetProcessor.processTweets(tweets_for_training)

"""
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

#vecto = CountVectorizer()

#vecto.fit(preprocessed_tweets)
#vect = vecto.transform(preprocessed_tweets).toarray()

"""








