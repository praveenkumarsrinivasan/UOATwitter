import csv

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
Dump the following details of a person into a csv file
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
