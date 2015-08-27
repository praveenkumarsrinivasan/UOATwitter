import tweepy
import csv
import re


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
    timeline = api.user_timeline(screen_name = twitter_handle,
        since_id = last_tweet_id, count = min_count)

    tweets_dict_list = []
    for tweet in timeline:
        tweets_dict_list.append(get_tweet_details(tweet))

    return tweets_dict_list


'''
Gets tweets till the given tweet id
'''
def get_tweets_till(api, twitter_handle, till_tweet_id):
    timeline = api.user_timeline(screen_name = twitter_handle,
        max_id = till_tweet_id, count = min_count)

    tweets_dict_list = []
    for tweet in timeline:
        tweets_dict_list.append(get_tweet_details(tweet))

    return tweets_dict_list


'''
Gets the latest tweets for the given tweet handle or user
'''
def get_latest_tweets(api, twitter_handle):
    timeline = api.user_timeline(screen_name = twitter_handle, count = min_count)

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
Gets the latest tweets from a given country
'''
def latest_tweets_by_location(api, location, location_type):
    results = []
    #granularity = poi, neighborhood, city, admin or country
    places = api.geo_search(query = location, granularity = location_type)
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


    ## Get the tweet with id
    tweet_id = "621338929208266752"
    #dump_tweets(get_tweet_by_id(api, tweet_id), tweet_id)


    ## Get the tweets that contain the search term 'movies'
    search_term = "movies"
    search_term = "movies or movie"
    #dump_tweets(search_tweets(api, search_term), search_term)
    ## Get the tweets that contain the following search terms ['movies', 'restaurants']


    ## by location - poi, neighborhood, city, admin or country
    ## Get the latest tweets from New Zealand
    location = "New Zealand"
    location_type = "country"
    dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ## Get the latest tweets from Auckland
    location = "Auckland"
    location_type = "city"
    dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ## Get the tweets from the given lat-long
    location = "Queen Street, Auckland, New Zealand" ##queen street - lat log
    location_type = "neighborhood"
    dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ##Get the tweets from the given lat-long region
    location = "12.9881347,77.73179549999998" ##queen street - lat log
    location_type = "neighborhood"
    location_type = "city"
    #dump_tweets(latest_tweets_by_location(api, location, location_type), location)

    ## Get the trending topics
    ## Get the trending topics by location - WOEID(Where on Earth ID)


if __name__ == '__main__':
    main()


