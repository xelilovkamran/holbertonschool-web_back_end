#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Union


def sum_mixed_list(sum_mixed_list: Union[int, float]) -> float:
    """Sum the values of a list of floats and integers."""
    return sum(sum_mixed_list)
