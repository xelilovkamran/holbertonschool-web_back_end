#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum the values of a list of floats."""
    return sum(input_list)
