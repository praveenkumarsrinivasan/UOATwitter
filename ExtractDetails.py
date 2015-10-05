import re 
import json

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
    user_dict['statuses_count'] = user.statuses_count
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


def get_place_details(place):
    place_dict = {}

    place_dict['country_code'] = place.country_code
    place_dict['country'] = place.country
    place_dict['place_type'] = place.place_type
    place_dict['bounding_box_type'] = place.bounding_box.type
    place_dict['bounding_box_coordinates'] = place.bounding_box.coordinates
    place_dict['contained_within'] = place.contained_within
    place_dict['full_name'] = place.full_name
    place_dict['id'] = place.id
    place_dict['name'] = place.name
    place_dict['attributes'] = place.attributes

    return place_dict


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

    if tweet.place != None:
        tweets_dict['place'] = get_place_details(tweet.place)
    else:
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

