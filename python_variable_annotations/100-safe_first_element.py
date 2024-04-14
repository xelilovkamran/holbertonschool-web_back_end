#!/usr/bin/env python3

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a list if it's not empty."""
    if lst:
        return lst[0]
    return None
