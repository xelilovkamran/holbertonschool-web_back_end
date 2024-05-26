#!/usr/bin/env python3
"""Log stats
"""

from pymongo import MongoClient

with MongoClient() as client:
    collection = client.logs.nginx
    print(f"{collection.find().count()} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection.find({'method': 'GET'}).count()}")
    print(f"\tmethod POST: {collection.find({'method': 'POST'}).count()}")
    print(f"\tmethod PUT: {collection.find({'method': 'PUT'}).count()}")
    print(f"\tmethod PATCH: {collection.find({'method': 'PATCH'}).count()}")
    print(f"\tmethod DELETE: {collection.find({'method': 'DELETE'}).count()}")
    print(
        f"{collection.find({'method': 'GET', "path": "/status"}).count()} status check")
