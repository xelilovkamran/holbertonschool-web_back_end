#!/usr/bin/env python3

from typing import Sequence, Any, Optional, Union


def safe_first_element(lst: list[Any]) -> Union[Any, None]:
    """Return the first element of a list if it's not empty."""
    if lst:
        return lst[0]
    else:
        return None
