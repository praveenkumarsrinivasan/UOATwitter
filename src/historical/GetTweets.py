import json
from ..utils.TwitterApp import *
from ..utils.ExtractDetails import *

'''
Gets tweets till the given tweet id
'''
def get_tweets_till(api, twitter_handle, till_tweet_id):
    timeline = api.user_timeline(
            screen_name = twitter_handle,
            max_id = till_tweet_id,
            count = min_count)

    tweets_dict_list = []
    for tweet in timeline:
        tweets_dict_list.append(get_tweet_details(tweet))

    return tweets_dict_list


'''
Gets the latest tweets for the given tweet handle or user
'''
def get_latest_tweets(api, twitter_handle):
    timeline = api.user_timeline(
            screen_name = twitter_handle,
            count = min_count)

    tweets_dict_list = []
    for tweet in timeline:
        tweets_dict_list.append(get_tweet_details(tweet))

    return tweets_dict_list


'''
Gets the last n tweets for the given twitter handle
'''
def get_last_n_tweets(api, twitter_handle, n):
    latest_tweets = get_latest_tweets(api, twitter_handle)
    if n > min_count:
        while n > min_count:
            n = n - min_count
            last_tweet_id = latest_tweets[-1]['tweet_id']
            latest_tweets.extend(get_tweets_till(api, twitter_handle, last_tweet_id))

    return latest_tweets


'''
Gets the tweet for the given tweet id
'''
def get_tweet_by_id(api, tweet_id):
    return [get_tweet_details(api.get_status(tweet_id))]


'''
Gets tweet by Latitude and Longitude
example location = "12.9881347,77.73179549999998,8km" ##queen street - lat log
'''
def latest_tweets_by_latlong(api, latlong_str):
    results = []
    tweets = tweepy.Cursor(
            api.search,
            geocode = latlong_str,
            lang = "en",
        ).items(min_count)
    for tweet in tweets:
        results.append(get_tweet_details(tweet))
    return results


'''
Get locations for a given latlong position where trending topics are available
'''
def get_trending_location(api, lat_str, long_str):
    trending_locations = api.trends_closest(
            lat_str,
            long_str)

    return trending_locations


'''
Get Trends for the given WOEID
'''
def get_trends_by_woeid(api, woeid):
    trends = api.trends_place(woeid)
    return trends


'''
Gets the latest tweets from a given location
'''
def latest_tweets_by_location(api, location, location_type):
    #granularity = poi, neighborhood, city, admin or country
    places = api.geo_search(
            query = location,
            granularity = location_type)
    place_id = places[0].id

    # print places

    tweets = tweepy.Cursor(
            api.search,
            q = 'place:' + place_id,
            lang = "en",
        ).items(min_count)

    results = []
    for tweet in tweets:
        results.append(get_tweet_details(tweet))

    return results


