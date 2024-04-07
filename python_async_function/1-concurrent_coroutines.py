#!/usr/bin/env python3
"""Concurrent coroutines"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays in ascending order"""
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
