import time
import json
from tweepy.streaming import StreamListener
from pymongo import MongoClient
from ..utils.TwitterApp import *

'''
There are different kinds of streams: public stream, user stream, multi-user(site) streams
'''

'''
#Listener Class Override
#sets up a connection and runs for the given time
    #http://stats.seandolinar.com/collecting-twitter-data-using-a-python-stream-listener/
'''
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
                # saveFile = open('raw_tweets.json', 'a')
                # saveFile.write(data)
                # saveFile.close()
                
                'Insert Into DB'
                collection.insert(json.loads(data))
                return True
            except BaseException, e:
                print 'failed ondata,', str(e)
                return False
        exit()

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing...'


'''
#Listener Class Override
#sets up a connection and reads data
    #http://code.runnable.com/Us9rrMiTWf9bAAW3/how-to-stream-data-from-twitter-with-tweepy-for-python
    #https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
    #https://github.com/tweepy/examples/blob/master/streamwatcher.py
'''
class StdOutListener(StreamListener):
    def __init__(self, collection_name):
        self.collection_name = collection_name

    def on_data(self, data):
        client = MongoClient('localhost', 27017)
        db = client['twitter_db']
        collection = db[self.collection_name]

        try:
            'Save to Text File'
            # saveFile = open('raw_tweets.json', 'a')
            # saveFile.write(data)
            # saveFile.close()

            'Insert Into DB'
            collection.insert(json.loads(data))
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            return False

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing ...'

