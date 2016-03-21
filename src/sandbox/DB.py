from pymongo import MongoClient
import json

def insert_data(tweets):
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    collection = db['twitter_collection']

    tweets = json.loads(tweets)
    res = collection.insert(tweets)
    
    return res

if __name__ == '__main__':
    insert_data(tweets)
