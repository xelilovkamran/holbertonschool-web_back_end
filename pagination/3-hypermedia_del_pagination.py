#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._dataset = None
        self._indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset method that reads and caches the dataset from a CSV file.
        """
        if self._dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self._dataset = dataset[1:]

        return self._dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns the dataset indexed by sorting position, starting at 0.
        """
        if self._indexed_dataset is None:
            dataset = self.dataset()
            self._indexed_dataset = {
                i: row for i, row in enumerate(dataset[:1000])
            }
        return self._indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Any]:
        """ 
        Returns a dictionary containing pagination information.
        """
        assert 0 <= index < len(self.dataset()), "Index out of range."

        indexed_dataset = self.indexed_dataset()
        data = []

        current_index = index
        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
