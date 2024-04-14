#!/usr/bin/env python3
"""Module for safe_first_element function."""

from typing import Iterable, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Iterable[Any]) -> Union[Any, None]:
    """Gets the first element of a list."""
    if lst:
        return lst[0]
    else:
        return None
