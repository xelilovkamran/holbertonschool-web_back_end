#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing a string and its length."""
    return [(i, len(i)) for i in lst]
