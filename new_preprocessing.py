import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
#nltk.download(stopwords)
from preprocessing import cleaned_test_tweets
#from Training_dataset import cleaned_training_tweets



class pre_process_tweets:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def preprocessed_tweets(self, list_of_unprocessed_tweets):
        processed_tweets = []
        for twe in list_of_unprocessed_tweets:
            processed_tweets.append(self._preprocess_tweets(twe))
        return processed_tweets

    def _preprocess_tweets(self, twe):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        twe = twe.lower()
        # Removing punctuations in string, Using loop + punctuation string
        for ele in twe:
            if ele in punc:
                twe = twe.replace(ele, "")
        words = twe.split(" ")
        filtered_sentence = []
        porter = PorterStemmer()
        for w in words:
            w = porter.stem(w)
            if w not in self.stop_words and len(w) > 1:
                filtered_sentence.append(w)
        return filtered_sentence


tweet_processor = pre_process_tweets()
preprocessed_test_tweets = tweet_processor.preprocessed_tweets(cleaned_test_tweets)     #list of list



