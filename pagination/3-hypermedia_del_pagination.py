#!/usr/bin/env python3
"""Perform deletion-resilient hypermedia pagination."""

import csv
from typing import List, Dict, Any


class Server:
    """Class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE, mode='r') as file:
                reader = csv.reader(file)
                dataset = list(reader)
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return a dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Any]:
        """Get hypermedia pagination data.

        Args:
            index (int): The starting index of the page.
            page_size (int): The number of records per page.

        Returns:
            Dict[str, Any]: A dictionary containing the index, next index, page size, and data.
        """
        assert 0 <= index < len(self.dataset()), "Index out of bounds"

        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        i = index
        while len(indexed_page) < page_size and i < len(self.dataset()):
            if i in indexed_dataset:
                indexed_page[i] = indexed_dataset[i]
            i += 1

        data = list(indexed_page.values())
        page_indices = indexed_page.keys()

        return {
            'index': index,
            'next_index': max(page_indices) + 1,
            'page_size': len(data),
            'data': data
        }
