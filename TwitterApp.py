import tweepy


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
    # api = tweepy.API(auth)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                               wait_on_rate_limit_notify=True)

    return api



