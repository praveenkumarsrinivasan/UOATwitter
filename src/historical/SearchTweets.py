import tweepy
from ..utils.TwitterApp import *
from ..utils.ExtractDetails import *


'''
Gets the tweets which matches the given search query
'''
def search_tweets(api, query):
    results = []

    #tweets = api.search(
            #q = query,
            #lang = "en",
            #count = min_count,
            #show_user = "true"
        #)
    #for tweet in tweets:
        #results.append(get_tweet_details(tweet))

    tweets = tweepy.Cursor(
            api.search,
            q = query,
            lang = "en",
        ).items(min_count)
    for tweet in tweets:
        results.append(get_tweet_details(tweet))

    return results


'''
Gets the tweets which matches the given search query from a given location
'''
def search_tweets_by_location(api, query, latlong_str):
    results = []

    tweets = tweepy.Cursor(
            api.search,
            q = query,
            geocode = latlong_str,
            lang = "en",
        ).items(min_count)
    for tweet in tweets:
        results.append(get_tweet_details(tweet))

    return results


'''
Gets the tweets which matches the given search query for a given user
'''
def search_user_tweets(api, twitter_handle, query):
    results = []

    #tweets = api.search(
            #q = query,
            #lang = "en",
            #count = min_count,
            #show_user = "true"
        #)
    #for tweet in tweets:
        #results.append(get_tweet_details(tweet))

    tweets = tweepy.Cursor(
            api.search,
            id = twitter_handle,
            q = query,
            lang = "en",
        ).items(min_count)

    for tweet in tweets:
        results.append(get_tweet_details(tweet))

    return results


