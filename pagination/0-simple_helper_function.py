#!/usr/bin/env python3
"""
Return a tuple of size two containing
a start index and an end index.
The function calculates the start index 
and end index for the given page and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Simple helper function """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)
