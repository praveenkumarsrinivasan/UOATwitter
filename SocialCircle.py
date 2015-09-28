from TwitterApp import *
from ExtractDetails import *


'''
Get the user id for the given Screen Name
'''
def get_user_id(api, twitter_handle):
    user = api.get_user(screen_name=twitter_handle)
    return user.id


'''
Get the people of interest(following) for a person
'''
def get_following_details_db(api, twitter_handle):
    users = tweepy.Cursor(
            api.friends,
            screen_name=twitter_handle
        ).items(5000)

    return users


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
def get_extended_following_details_db(api, twitter_handle, following):
    results = []
    results.extend(following)
    for f in following:
        try:
            print 'Getting the details for ' + f['screenname']
            users = tweepy.Cursor(
                    api.friends,
                    screen_name=f['screenname']
                ).items(5000)
            results.extend(users)
        except tweepy.error.RateLimitError as e:
            print("rate limit  error : " + str(e))
        except tweepy.TweepError as e:
            # Just exit if any error
            print("error : " + str(e))
    return results


'''
Get the people of interest(following) for the list of people of interest for a person
'''
def get_extended_following_details(api, twitter_handle, following):
    results = []
    results.extend(following)
    for f in following:
        try:
            print 'Getting the details for ' + f['screenname']
            users = tweepy.Cursor(
                    api.friends,
                    screen_name=f['screenname']
                ).items(5000)
            for user in users:
                print user.screen_name
                results.append(get_user_details(user))
            # print 'sleeping for 60'
            # time.sleep(60)
        except tweepy.error.RateLimitError as e:
            print("rate limit  error : " + str(e))
            # dump_following(twitter_handle + '_' + flag, results)
            # print 'sleeping for 60*5'
            # time.sleep((60 * 5))
            # time.sleep((60 * 15) + 5)
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
    return results


'''
Get the followers for a person
'''
def get_followers_details_db(api, user_name):
    users = tweepy.Cursor(api.followers, screen_name=user_name)
    return users


'''
get the followers for a person
'''
def get_followers_details(api, user_name):
    users = []
    for user in tweepy.cursor(api.followers, screen_name=user_name).items():
        print user.screen_name
        users.append(user)
    return users


