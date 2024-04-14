#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list if it's not empty."""
    if lst:
        return lst[0]
    return None
