from final_training_set import preprocessed_training_set
import nltk

word_features = []

def buildVocabulary(preprocessed_training_set):
    all_words = []
    for (ws, senti) in preprocessed_training_set:
        all_words.extend(ws)
    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()
    return word_features

def extract_features(take_tweet):
    tweet_words = set(take_tweet)
    features = {}
    for take_word in word_features:
        features['contains(%s)' % take_word] = (take_word in tweet_words)
    return features

word_fs = buildVocabulary(preprocessed_training_set)
training_features = nltk.classify.apply_features(extract_features, preprocessed_training_set)






