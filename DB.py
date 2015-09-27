from pymongo import MongoClient
import json

def insert_data(tweets):
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    collection = db['twitter_collection1']

    tweets = json.loads(tweets)
    res = collection.insert(tweets)
    
    return res

if __name__ == '__main__':
    tweets = {}
    tweets["name"] = "one"
    tweets["time"] = "12pm"
    tweets = json.dumps(tweets, ensure_ascii=False)
    insert_data(tweets)
