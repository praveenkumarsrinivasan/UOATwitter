import tweepy
import csv
import re
import time


#my twitter api connection parameters
consumer_key = 'XTfkoGOB2nSBjsntLIGbpN55R'
consumer_secret = 'EXB6soJyHp0yRpzpnVaYJVmotnV4aiVII6DifSEX5VP1vdkHMU'
access_token = '187548221-ryYtHuDkSbbLFZxdlalrBGEoBDEhxD2T9gsfUZvM'
access_token_secret = 'kF0PLt5jGrbSLQFYl7z0SWu0aRMIzT5LmWqit4KzbCAvP'


#the number of tweets to fetch in each api request
min_count = 200


'''
authenticate the Twitter API
returns the Twitter api object
'''
def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

'''
Get User Details
'''
def get_user_details(user):

    user_dict = {}

    user_dict['user_id'] = user.id
    user_dict['username'] = user.name.encode('utf8')
    user_dict['screenname'] = user.screen_name.encode('utf8')
    user_dict['followers_count'] = user.followers_count
    user_dict['friends_count'] = user.friends_count
    user_dict['listed_count'] = user.listed_count
    user_dict['favourites_count'] = user.favourites_count
    user_dict['geo_enabled'] = user.geo_enabled
    user_dict['following'] = user.following
    user_dict['location'] = user.location.encode('utf8')
    if user.time_zone != None:
        user_dict['time_zone'] = user.time_zone.encode('utf8')
    else:
        user_dict['time_zone'] = ''

    # user_dict['text'] = re.sub(r'\s+', ' ', str(user.text.encode('utf8')).replace('"', ''))
    #user_dict['text'] = user.text.encode('utf8')

    user_dict['created_at'] = user.created_at.strftime('%Y-%m-%d %H:%M')

    # user_dict['place'] = user.place
    # user_dict["coordinates"] = user.coordinates
    # user_dict["geo"] = user.geo

    # user_dict["favorited"] = user.favorited
    # user_dict["favorite_count"] = user.favorite_count

    # user_dict["retweeted"] = user.retweeted
    # user_dict["retweet_count"] = user.retweet_count

    # user_dict["in_reply_to_screen_name"] = user.in_reply_to_screen_name
    # user_dict["in_reply_to_status_id"] = user.in_reply_to_status_id
    # user_dict["in_reply_to_user_id"] = user.in_reply_to_user_id

    # user_dict["contributors"] = user.contributors
    # user_dict["source"] = user.source.encode('utf8')
    # user_dict["truncated"] = user.truncated

    # user_dict["hashtags"] = user.entities['hashtags']
    # user_dict["urls"] = user.entities['urls']
    # user_dict["symbols"] = user.entities['symbols']
    # user_dict["user_mentions"] = user.entities['user_mentions']

    return user_dict


'''
returns a dict of necessary attributes for a given tweet
'''
def get_tweet_details(tweet):

    tweets_dict = {}

    tweets_dict['tweet_id'] = tweet.id

    tweets_dict['user_id'] = tweet.user.id
    tweets_dict['username'] = tweet.user.name.encode('utf8')
    tweets_dict['screenname'] = tweet.user.screen_name.encode('utf8')
    tweets_dict['followers_count'] = tweet.user.followers_count
    tweets_dict['friends_count'] = tweet.user.friends_count
    tweets_dict['listed_count'] = tweet.user.listed_count
    tweets_dict['favourites_count'] = tweet.user.favourites_count
    tweets_dict['geo_enabled'] = tweet.user.geo_enabled
    tweets_dict['following'] = tweet.user.following
    tweets_dict['location'] = tweet.user.location.encode('utf8')

    tweets_dict['text'] = re.sub(r'\s+', ' ', str(tweet.text.encode('utf8')).replace('"', ''))
    #tweets_dict['text'] = tweet.text.encode('utf8')

    tweets_dict['created_at'] = tweet.created_at.strftime('%Y-%m-%d %H:%M')

    tweets_dict['place'] = tweet.place
    tweets_dict["coordinates"] = tweet.coordinates
    tweets_dict["geo"] = tweet.geo

    tweets_dict["favorited"] = tweet.favorited
    tweets_dict["favorite_count"] = tweet.favorite_count

    tweets_dict["retweeted"] = tweet.retweeted
    tweets_dict["retweet_count"] = tweet.retweet_count

    tweets_dict["in_reply_to_screen_name"] = tweet.in_reply_to_screen_name
    tweets_dict["in_reply_to_status_id"] = tweet.in_reply_to_status_id
    tweets_dict["in_reply_to_user_id"] = tweet.in_reply_to_user_id

    tweets_dict["contributors"] = tweet.contributors
    tweets_dict["source"] = tweet.source.encode('utf8')
    tweets_dict["truncated"] = tweet.truncated

    tweets_dict["hashtags"] = tweet.entities['hashtags']
    tweets_dict["urls"] = tweet.entities['urls']
    tweets_dict["symbols"] = tweet.entities['symbols']
    tweets_dict["user_mentions"] = tweet.entities['user_mentions']

    return tweets_dict


'''
Gets tweets from a given tweet id
'''
def get_tweets_since(api, twitter_handle, last_tweet_id):
    timeline = api.user_timeline(
            screen_name = twitter_handle,
            since_id = last_tweet_id,
            count = min_count)

    tweets_dict_list = []
    for tweet in timeline:
        tweets_dict_list.append(get_tweet_details(tweet))

    return tweets_dict_list


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
Gets the latest tweets from a given country
'''
def latest_tweets_by_location(api, location, location_type):
    results = []
    #granularity = poi, neighborhood, city, admin or country
    places = api.geo_search(
            query = location,
            granularity = location_type)
    place_id = places[0].id

    print places

    tweets = tweepy.Cursor(
            api.search,
            q = 'place:' + place_id,
            lang = "en",
        ).items(min_count)
    for tweet in tweets:
        results.append(get_tweet_details(tweet))

    return results


'''
Get tweets by Latitude and Longitude
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
Get the people of interest(following) for a person
'''
def get_following_details(api, twitter_handle):
    users = tweepy.Cursor(
            api.friends,
            screen_name=twitter_handle
        ).items(5000)

    results = []
    for user in users:
        results.append(get_user_details(user))

    return results


'''
Get the people of interest(following) for the list of people of interest for a person
'''
def get_extended_following_details(api, twitter_handle, following):
    flag = 0
    results = []
    results.extend(following)
    for f in following:
        print f
        try:
            print 'Getting the details for ' + f['screenname']
            users = tweepy.Cursor(
                    api.friends,
                    screen_name=f['screenname']
                ).items(5000)
            for user in users:
                print user.screen_name
                results.append(user)
            time.sleep(60)
        except tweepy.error.RateLimitError:
            flag = flag + 1
            print 'Pausing for rate limit ...'
            results = list(set(results))
            dump_following(twitter_handle + '_' + flag, results)
            time.sleep((60 * 5))
            # time.sleep((60 * 15) + 5)
    results = list(set(results))
    return results


'''
Get the followers for a person
'''
def get_followers_details(api, user_name):
    users = []
    for user in tweepy.Cursor(api.followers, screen_name=user_name).items():
        print user.screen_name
        users.append(user)
    return user


def get_all_tweets(api):
    a = api.home_timeline()


'''
print all the tweets in console friendly manner
'''
def print_tweets(tweets):
    for i in range(0, len(tweets)):
        print i+1, " :> ", tweets[i]['text']
    print tweets[-1]


'''
Dump the tweets into a csv file
'''
def dump_tweets(tweets, twitter_handle):
    header = ['tweet_id', 'user_id', 'username', 'screenname', 'followers_count', 'friends_count', 'listed_count', 'favourites_count', 'geo_enabled', 'following', 'location', 'text', 'created_at', 'place', 'coordinates', 'geo', 'favorited', 'favorite_count', 'retweeted', 'retweet_count', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_user_id', 'contributors', 'source', 'truncated', 'hashtags', 'urls', 'symbols', 'user_mentions']

    with open('output/%s_tweets.csv' % twitter_handle, 'wb') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for tweet in tweets:
            row = []
            for k in header:
                row.append(tweet[k])
            writer.writerow(row)


'''
'''
def dump_following(twitter_handle, following):
    with open('output/%s_following.csv' % twitter_handle, 'wb') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = following[0].keys()
        writer.writerow(header)
        for item in following:
            row = []
            for k in header:
                row.append(item[k])
            writer.writerow(row)

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
    #latest_tweets = get_latest_tweets(api, twitter_handle)
    #dump_tweets(latest_tweets, twitter_handle)


    ## Get the last 600 tweets from Jonathan Morison
    #last_n_tweets = get_last_n_tweets(api, twitter_handle, 600)
    #dump_tweets(last_n_tweets, twitter_handle)


    ## ID
    ## Get the tweet with id
    tweet_id = "621338929208266752"
    #dump_tweets(get_tweet_by_id(api, tweet_id), tweet_id)


    # Search terms
    ## Get the tweets that contain the search term 'movies'
    search_term = "movies"
    search_term = "movies or movie"
    #dump_tweets(search_tweets(api, search_term), search_term)
    ## Get the tweets that contain the following search terms ['movies', 'restaurants']


    ## Location - poi, neighborhood, city, admin or country
    ## Get the latest tweets from New Zealand
    location = "New Zealand"
    location_type = "country"
    #dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ## Get the latest tweets from Auckland
    location = "Auckland"
    location_type = "city"
    #dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ## Get the tweets from the given lat-long
    location = "Queen Street, Auckland, New Zealand" ##queen street - lat log
    location_type = "neighborhood"
    #dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ##Get the tweets from the given lat-long region
    location = "12.9881347,77.73179549999998,8km" ##queen street - lat log
    location_type = "ITPL Main Road LatLong"
    #dump_tweets(latest_tweets_by_latlong(api, location), location_type)


    ## Trending Topics
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


    ## Search term and Location
    location = "12.9881347,77.73179549999998,8km" ##queen street - lat log
    location_type = "ITPL Main Road LatLong"
    query = "#movies"
    # dump_tweets(search_tweets_by_location(api, query, location), location_type)


    ##get social circle of a person
    twitter_handle = 'anjaligupta2910'
    following = get_following_details(api, twitter_handle)
    dump_following(twitter_handle, following)
    ##get followers
    # followers = get_followers_details(api, twitter_handle)

    ##get the extended social circle of a person
    extended_following = get_extended_following_details(api, twitter_handle, following)
    dump_following(twitter_handle, extended_following)


if __name__ == '__main__':
    main()


