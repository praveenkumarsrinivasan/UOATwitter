import tweepy
from ReadAccessInfo import *

#the number of tweets to fetch in each api request
min_count = 200 #not used currently


def get_auth(access_index=5):
    access_obj = get_access_info(access_index)
    consumer_key = access_obj['consumer_key']
    consumer_secret = access_obj['consumer_secret']
    access_token = access_obj['access_token']
    access_token_secret = access_obj['access_token_secret']

    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


'''
authenticate the Twitter API
returns the Twitter api object
'''
def authenticate(access_index=5):
    auth = get_auth(access_index)
    api = tweepy.API(
                auth,
                wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True
            )

    return api



