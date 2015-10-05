import time
import json
from TwitterApp import *
from SocialCircle import *
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient


'''
There are different kinds of streams: public stream, user stream, multi-user(site) streams
'''

#Listener Class Override
#sets up a connection and runs for the given time
#http://stats.seandolinar.com/collecting-twitter-data-using-a-python-stream-listener/
class LimitListener(StreamListener):
    def __init__(self, collection_name, start_time, time_limit=60.0):
        self.time = start_time
        self.limit = time_limit
        self.collection_name = collection_name

    def on_data(self, data):
        client = MongoClient('localhost', 27017)
        db = client['twitter_db']
        collection = db[self.collection_name]

        while (time.time() - self.time) < self.limit:
            try:
                'Save to File'
                saveFile = open('raw_tweets.json', 'a')
                saveFile.write(data)
                saveFile.close()
                
                'Insert Into DB'
                # data = json.dumps(data, ensure_ascii=False)
                collection.insert(json.loads(data))
                return True

            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass
        exit()

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive


#Listener Class Override
#resposible for receiving data
#http://code.runnable.com/Us9rrMiTWf9bAAW3/how-to-stream-data-from-twitter-with-tweepy-for-python
#https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
#https://github.com/tweepy/examples/blob/master/streamwatcher.py
class StdOutListener(tweepy.StreamListener):
    def __init__(self, collection_name):
        self.collection_name = collection_name

    def on_data(self, data):
        client = MongoClient('localhost', 27017)
        db = client['twitter_db']
        collection = db[self.collection_name]

        try:
            saveFile = open('raw_tweets.json', 'a')
            saveFile.write(data)
            saveFile.close()

            'Insert Into DB'
            # data = json.dumps(data, ensure_ascii=False)
            collection.insert(json.loads(data))

            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            return False

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'


if __name__ == '__main__':
    auth = get_auth()
    api = authenticate()

    track_location_latlong = [[-122.75, 36.8, -121.75, 37.8], [-74,40,-73,41]]

    track_user_list = ['anjaligupta2910', 'MKBHD']
    track_user_id_list = ['575930104']
    track_user_id_list = []
    for user in track_user_list:
        track_user_id_list.append(str(get_user_id(api, user)))
    print track_user_id_list

    track_keyword_list = ['programming']

    # std_listener = StdOutListener('twitter_keyword_collection')
    # std_stream = tweepy.Stream(auth, std_listener)
    # std_stream.filter(track=track_keyword_list, async=True)
    # std_stream.filter(track=track_keyword_list)

    # limit_listener = LimitListener('twitter_keyword_collection', time.time(), time_limit=60.0)
    # limit_stream = Stream(auth, limit_listener) #initialize Stream object with a time out limit
    # limit_stream.filter(track=track_keyword_list, languages=['en'])  #call the filter method to run the Stream Object

    # std_listener1 = StdOutListener('twitter_user_collection')
    # std_stream1 = tweepy.Stream(auth, std_listener1)
    # std_stream1.filter(follow=track_user_id_list)

    # limit_listener1 = LimitListener('twitter_user_collection', time.time(), time_limit=60.0)
    # limit_stream1 = Stream(auth, limit_listener1) #initialize Stream object with a time out limit
    # limit_stream1.filter(follow=track_user_id_list, languages=['en'])  #call the filter method to run the Stream Object

    limit_listener2 = LimitListener('twitter_location_collection', time.time(), time_limit=60.0)
    limit_stream2 = Stream(auth, limit_listener2) #initialize Stream object with a time out limit
    limit_stream2.filter(locations=track_location_latlong, languages=['en'])  #call the filter method to run the Stream Object

