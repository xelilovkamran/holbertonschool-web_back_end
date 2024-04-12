#!/usr/bin/env python3
""" LFU caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Initialize the LFUCache instance. """
        self.lfu_elements = {}
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if not key or not item:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.lfu_elements[key] += 1
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequently used key
            lfu_key = list(self.cache_data.keys())[0]
            min_frequency = self.lfu_elements[lfu_key]

            for k, freq in self.lfu_elements.items():
                if freq < min_frequency:
                    lfu_key = k
                    min_frequency = freq

            # Remove the least frequently used key
            self.cache_data.pop(lfu_key)
            self.lfu_elements.pop(lfu_key)
            print(f"DISCARD: {lfu_key}")

            # Add the new key-value pair
            self.cache_data[key] = item
            self.lfu_elements[key] = 1
        else:
            # Add the new key-value pair
            self.cache_data[key] = item
            self.lfu_elements[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.lfu_elements[key] += 1
            return self.cache_data[key]
        return None
