#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the key and value squared."""
    return (k, v ** 2)
