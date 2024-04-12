#!/usr/bin/env python3
""" Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCach class"""

    def put(self, key, item):
        """ Add an item in the cache """
        if key == None or item == None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if not key == None and key in self.cache_data:
            return self.cache_data[key]
