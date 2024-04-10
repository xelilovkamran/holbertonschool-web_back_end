#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator, Any


async def numbers(numbers: int) -> AsyncGenerator[int, None]:
    """Generate numbers from 0 to numbers."""
    for i in range(numbers):
        yield i


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate 10 random numbers between 0 and 10 with a 1 second delay between each number."""
    async for i in numbers(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
