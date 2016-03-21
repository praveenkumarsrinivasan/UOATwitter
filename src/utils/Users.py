from TwitterApp import *
from DumpData import *
from ExtractDetails import *
from pymongo import MongoClient

def dump_users_details(api):
    with open('data/users.txt') as f:
        users = f.readlines()

    for user in users:
        user = user.strip()
        if user != '':
            user = api.get_user(screen_name=user)
            user_details = get_user_details(user)
            dump_user_db(user, user_details, 'twitter_user_collection')


def get_user_id(user):
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    user = list(db.twitter_user_collection.find({"screenname": user}, {"user_id" : 1}))
    if len(user) > 0:
        return user[0]['user_id']
    else:
        return -1


def get_user_ids():
    with open('data/users.txt') as f:
        users = f.readlines()

    for user in users:
        user = user.strip()
        print user, get_user_id(user)


if __name__ == "__main__":
    api = authenticate()
    # dump_users_details(api)
    # print get_user_id('anjaligupta2910')
    get_user_ids()
