#!/usr/bin/env python3
""" LIFO caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.mru_keys:
                self.mru_keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.mru_keys.pop(3)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.mru_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            returned_value = self.cache_data[key]
            self.mru_keys.remove(key)
            self.mru_keys.append(key)
            return returned_value
