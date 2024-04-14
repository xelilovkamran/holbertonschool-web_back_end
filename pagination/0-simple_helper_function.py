#!/usr/bin/env python3
""" Simple helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Return a tuple of size two containing
    a start index and an end index.
    The function calculates the start index 
    and end index for the given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
