#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a number by n."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
