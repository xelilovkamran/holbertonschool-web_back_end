#!/usr/bin/env python3
"""Log stats
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """Prints some stats about Nginx logs stored in mongo_collection
    """
    print(f"{mongo_collection.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {mongo_collection.find({'method': 'GET'}).count()}")
    print(
        f"\tmethod POST: {mongo_collection.find({'method': 'POST'}).count()}")
    print(f"\tmethod PUT: {mongo_collection.find({'method': 'PUT'}).count()}")
    print(
        f"\tmethod PATCH: {mongo_collection
                           .find({'method': 'PATCH'})
                           .count()}")
    print(
        f"\tmethod DELETE: {mongo_collection
                            .find({'method': 'DELETE'})
                            .count()}")
    print(
        f"{mongo_collection
           .find({'method': 'GET', "path": "/status"})
           .count()} status check")


if __name__ == "__main__":
    collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(collection)
