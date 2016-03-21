from tweepy import Stream
from Listeners import *
from ..utils.TwitterApp import *

'''
Fetch the twitter stream for the given lat long and store the same into db
'''
def get_location_stream(track_location_latlong, stream_type_flag = 'Time'):
    if stream_type_flag == 'Std':
        std_listener = StdOutListener('twitter_location_collection')
        std_stream = tweepy.Stream(auth, std_listener)
        std_stream.filter(locations=track_location_latlong, async=True)
    elif stream_type_flag == 'Time':
        limit_listener = LimitListener('twitter_location_collection', time.time(), time_limit=60.0)
        limit_stream = Stream(auth, limit_listener) #initialize Stream object with a time out limit
        limit_stream.filter(locations=track_location_latlong, languages=['en'])  #call the filter method to run the Stream Object


'''
Fetch the twitter stream of the given users handles by fetching the corresponding twitter ids, store the same into db
'''
def get_users_stream(track_user_id_list, stream_type_flag = 'Time'):
    if stream_type_flag == 'Std':
        std_listener = StdOutListener('twitter_user_collection')
        std_stream = tweepy.Stream(auth, std_listener)
        std_stream.filter(follow=track_user_id_list, async=True)
        # std_stream1.filter(follow=track_user_id_list)
    elif stream_type_flag == 'Time':
        limit_listener = LimitListener('twitter_user_collection', time.time(), time_limit=60.0)
        limit_stream = Stream(auth, limit_listener) #initialize Stream object with a time out limit
        limit_stream.filter(follow=track_user_id_list, languages=['en'])  #call the filter method to run the Stream Object


'''
Fetch the twitter stream for the given keywords and store the same into the db
'''
def get_keywords_stream(stream_type_flag = 'Time'): #Time|Std
    if stream_type_flag == 'Std':
        std_listener = StdOutListener('twitter_keyword_collection')
        std_stream = tweepy.Stream(auth, std_listener)
        std_stream.filter(track=track_keyword_list, async=True)
        # std_stream.filter(track=track_keyword_list)
    elif stream_type_flag == 'Time':
        limit_listener = LimitListener('twitter_keyword_collection', time.time(), time_limit=60.0)
        limit_stream = Stream(auth, limit_listener) #initialize Stream object with a time out limit
        limit_stream.filter(track=track_keyword_list, languages=['en'])  #call the filter method to run the Stream Object


if __name__ == '__main__':
    auth = get_auth(4)
    get_location_stream([])

