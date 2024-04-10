#!/usr/bin/env python3
"""program that creates an async generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator that yields random numbers
    between 0 and 10 every second for 10 seconds.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
