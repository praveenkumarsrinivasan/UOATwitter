import math
import json
from TwitterApp import *
from ExtractDetails import *
from DumpData import *

def dump_location_details(api):
    with open('data/cities.txt') as f:
        cities = f.readlines()

    for city in cities[-3:]:
        city = city.strip()
        if city != '':
            places = api.geo_search(
                    query = city,
                    granularity = 'city')

            res = get_place_details(places[0])
            dump_location_db(res, 'twitter_city_collection')


def get_latlong_details(city):
    lat_long = []

    client = MongoClient('localhost', 27017)
    db = client['twitter_db']
    city_obj = list(db.twitter_city_collection.find({"full_name" : {'$regex' : '.*'+city+'.*'}}))
    if len(city_obj) > 0:
        lat_long.extend(city_obj[0]['bounding_box_coordinates'][0][0])
        lat_long.extend(city_obj[0]['bounding_box_coordinates'][0][3])

        lat_long[1] = math.floor(lat_long[1])
        lat_long[3] = math.ceil(lat_long[3])

    return lat_long


def get_latlong_cities():
    with open('data/cities.txt') as f:
        cities = f.readlines()

    for city in cities:
        city = city.strip()
        print city, get_latlong_details(city)

if __name__ == "__main__":
    api = authenticate(2)
    # dump_location_details(api)
    # print get_latlong_details('New York')
    get_latlong_cities()


