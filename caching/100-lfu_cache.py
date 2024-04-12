#!/usr/bin/env python3
""" LFU caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Override superclass __init__ """
        self.lfu_elements = {}
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu_elements[key] += 1
            elif len(self.cache_data) >= self.MAX_ITEMS:
                frequently_used_key = list(self.cache_data.items())[0][0]
                for cache_item in self.lfu_elements.items():
                    if list(cache_item)[1] < self.lfu_elements[frequently_used_key]:
                        frequently_used_key = cache_item[0]

                self.cache_data.pop(frequently_used_key)
                self.cache_data[key] = item

                self.lfu_elements.pop(frequently_used_key)
                self.lfu_elements[key] = 1
                print("DISCARD: {}".format(frequently_used_key))
            else:
                self.cache_data[key] = item
                self.lfu_elements[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.lfu_elements[key] += 1
            return self.cache_data[key]
