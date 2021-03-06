from ..utils.TwitterApp import *
from ..utils.DumpData import *
from ..utils.ExtractDetails import *
from GetTweets import *
from SearchTweets import *
from SocialCircle import *

'''
Invoke the necessary functions and act as the point of entry to the code
Serves as the test script for the code
'''
def main():
    ## authenticate the api
    api = authenticate()


    ## Get the latest tweets from MKBHD
    twitter_handle = 'mkbhd'
    twitter_handle = 'tldtoday'
    twitter_handle = 'anjaligupta2910'
    # latest_tweets = get_latest_tweets(api, twitter_handle)
    # dump_tweets_db(latest_tweets, twitter_handle)
    # dump_tweets(latest_tweets, twitter_handle)


    ## Get the last 600 tweets from Jonathan Morison
    # last_n_tweets = get_last_n_tweets(api, twitter_handle, 600)
    # dump_tweets_db(last_n_tweets, twitter_handle)
    #dump_tweets(last_n_tweets, twitter_handle)


    ## ID
    ## Get the tweet with id
    tweet_id = "621338929208266752"
    # tweet = get_tweet_by_id(api, tweet_id)
    # dump_tweets_db(tweet, tweet_id)
    # dump_tweets(tweet, tweet_id)


    ### Location - poi, neighborhood, city, admin or country
    ## Get the latest tweets from New Zealand
    location = "New Zealand"
    location_type = "country"
    # tweets = latest_tweets_by_location(api, location, location_type)
    # dump_tweets_db(tweets, location)
    # dump_tweets(tweets, location)


    ## Get the latest tweets from Auckland
    location = "Auckland"
    location_type = "city"
    # tweets = latest_tweets_by_location(api, location, location_type)
    # dump_tweets_db(tweets, location)
    # dump_tweets(tweets, location)

    ## Get the tweets from the given lat-long
    location = "Queen Street, Auckland, New Zealand" ##queen street - lat log
    location_type = "neighborhood"
    # tweets = latest_tweets_by_location(api, location, location_type)
    # dump_tweets_db(tweets, location)
    # dump_tweets(tweets, location)

    ##Get the tweets from the given lat-long region
    location = "12.9881347,77.73179549999998,8km" ##queen street - lat log
    location_type = "LatLong"
    # tweets = latest_tweets_by_latlong(api, location)
    # dump_tweets_db(tweets, location_type)
    # dump_tweets(tweets, location_type)


    ### Trending Topics
    ## Get the daily trending topics
    lat_str = "12.9881347"
    long_str = "77.73179549999998"
    ## Get the locations where trending topics are available closest to the given LatLong
    # locations = get_trending_location(api, lat_str, long_str)
    ## WOEID(Where on Earth ID)
    # woeid = locations[0]['woeid']
    ## Get the trending topics by location - WOEID(Where on Earth ID)
    # trends = get_trends_by_woeid(api, woeid)
    ## TODO: dump trends


    ### Search terms
    ## Get the tweets that contain the search term 'movies'
    search_term = "movies"
    search_term = "movies or movie"
    print 'Searching Tweet for ', search_term
    tweets = search_tweets(api, search_term)
    dump_tweets_db(tweets, search_term)
    # dump_tweets(tweets, search_term)
    ## Get the tweets that contain the following search terms ['movies', 'restaurants']


    ## Search term and Location
    location = "12.9881347,77.73179549999998,8km" ##queen street - lat log
    location_type = "LatLong"
    query = "#itpl"
    print 'Searching tweets by location and query', location,
    # tweets = search_tweets_by_location(api, query, location)
    # dump_tweets_db(tweets, location_type)
    # dump_tweets(tweets, location_type)


    ##Search tweets of a given user
    twitter_handle = 'mkbhd'
    search_term = 'movies'
    #result = search_user_tweets(api, twitter_handle, search_term)
    #dump_tweets_db(result, twitter_handle)
    #dump_tweets(result, twitter_handle)


    ###Social Circle
    ##get social circle of a person
    twitter_handle = 'anjaligupta2910'
    # following = get_following_details(api, twitter_handle)
    # dump_user_db(twitter_handle, following)
    # dump_user(twitter_handle, following)
    ##get followers
    # followers = get_followers_details(api, twitter_handle)
    # dump_user_db(twitter_handle, followers)


    ##get the extended social circle of a person
    # extended_following = get_extended_following_details(api, twitter_handle, following)
    # dump_user_db(twitter_handle, extended_following)
    # dump_user(twitter_handle, extended_following)


if __name__ == '__main__':
    main()


