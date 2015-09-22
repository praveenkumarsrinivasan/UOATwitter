from TwitterApp import *
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

'''
There are different kinds of streams: public stream, user stream, multi-user(site) streams
'''

#Listener Class Override
#sets up a connection and runs for the given time
#http://stats.seandolinar.com/collecting-twitter-data-using-a-python-stream-listener/
class LimitListener(StreamListener):
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit

    def on_data(self, data):
        while (time.time() - self.time) < self.limit:
            try:
                saveFile = open('raw_tweets.json', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()

                return True
            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass


    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive


#Listener Class Override
#resposible for receiving data
#http://code.runnable.com/Us9rrMiTWf9bAAW3/how-to-stream-data-from-twitter-with-tweepy-for-python
#https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
#https://github.com/tweepy/examples/blob/master/streamwatcher.py
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            saveFile = open('raw_tweets.json', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()

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

    track_user_list = ['anjaliscorpio2910']
    track_keyword_list = ['programming']

    std_listener = StdOutListener()
    std_stream = tweepy.Stream(auth, std_listener)
    # std_stream.filter(track=track_keyword_list, async=True)
    std_stream.filter(track=track_keyword_list)

    # limit_listner = LimitListener(start_time, time_limit=20)
    # limit_stream = Stream(auth, limit_listener) #initialize Stream object with a time out limit
    # limit_stream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object

    # std_listener1 = StdOutListener()
    # std_stream1 = tweepy.Stream(auth, std_listener)
    # std_stream1.filter(track_user_list, track_keyword_list)

