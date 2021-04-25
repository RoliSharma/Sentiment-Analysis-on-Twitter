from Pre_training_tweets import preprocessed_training_tweets
from Training_dataset import sentiment_of_training_tweets

preprocessed_training_set = []

for i in range(len(preprocessed_training_tweets)):
    preprocessed_training_set.append((preprocessed_training_tweets[i], sentiment_of_training_tweets[i]))
