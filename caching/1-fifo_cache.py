""" FIFO caching """

from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_item)
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            return self.cache_data[key]
