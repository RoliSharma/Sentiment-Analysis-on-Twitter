# Sentiment-Analysis-on-Twitter
-Retrieving tweets using Tweepy API 
-Data preprocessing
-Feature Extraction 
-Training Dataset 
-Naive Bayes Classification 
-Output


# Tweepy API documentation

https://docs.tweepy.org/en/v3.10.0/api.html#API.search
API.search(q[, geocode][, lang][, locale][, result_type][, count][, until][, since_id][, max_id][, include_entities])
q – the search query string of 500 characters maximum, including operators. 
Queries may additionally be limited by complexity.

lang – Restricts tweets to the given language, given by an ISO 639-1 code.
 Language detection is best-effort.
 
result_type –
Specifies what type of search results you would prefer to receive.
 The current default is “mixed.” Valid values include:

mixed : include both popular and real time results in the response
recent : return only the most recent results in the response
popular : return only the most popular results in the response


count – The number of results to try and retrieve per page.

#Streaming With Tweepy
Tweepy makes it easier to use the twitter streaming api by handling authentication, connection, 
creating and destroying the session, reading incoming messages, and partially routing messages.


The Twitter streaming API is used to download twitter messages in real time. 
It is useful for obtaining a high volume of tweets, or for creating a live feed using a site
 stream or user stream.
 
In Tweepy, an instance of tweepy.Stream establishes a streaming session and routes messages to 
StreamListener instance. The on_data method of a stream listener receives all messages and calls
 functions according to the message type. The default StreamListener can classify most common
  twitter messages and routes them to appropriately named methods, but these methods are only
  stubs.

->Extended tweets to access non-truncated tweets


STEPS of DATA PREPROCESSING...


Tokenization — convert sentences to words
Removing unnecessary punctuation, tags
Removing stop words — frequent words such as ”the”, ”is”, etc. that do not have specific semantic
Stemming — words are reduced to a root by removing inflection through dropping unnecessary characters, usually a suffix.
Lemmatization — Another approach to remove inflection by determining the part of speech and utilizing detailed database of the language.