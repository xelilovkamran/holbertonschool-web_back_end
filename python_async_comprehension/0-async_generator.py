#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[Any, Any, Any]:
    """Generate 10 random numbers between 0 and 10 with a 1 second delay between each number."""
    async for i in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
