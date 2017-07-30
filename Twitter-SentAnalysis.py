
# coding: utf-8

# In[1]:

get_ipython().system(u'pip install tweepy')


# In[2]:

get_ipython().system(u'pip install -U textblob')
get_ipython().system(u'python -m textblob.download_corpora')


# In[3]:

import tweepy
from textblob import TextBlob


# The following information is available on [dev.twitter.com](https://dev.twitter.com)

# In[4]:

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)


# In[5]:

def sentiment(subject, num_tweets):
    # Checks if the sentiment for our quote is
    # positive or negative, returns True if
    # majority of valid tweets have positive sentiment
    list_of_tweets = user.search(subject, count=num_tweets)
    positive, null = 0, 0

    for tweet in list_of_tweets:
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null += 1
            next
        if blob.polarity > 0:
            positive += 1

    if positive > ((num_tweets - null)/2):
        return True


# In[6]:

# Ask user for a subject to perform sentiment analysis on
subject = raw_input('Enter the subject for which you wish to perform sentiment analysis on: ')


# In[7]:

num_tweets = int(input('How many tweets should I look through to determine the sentiment about %s? ' % (subject)))


# In[8]:

if sentiment(subject, num_tweets):
    print "%s has good sentiment on Twitter." % (subject)
    
if not sentiment(subject, num_tweets):
    print "%s has bad sentiment on Twitter." % (subject)


# In[ ]:



