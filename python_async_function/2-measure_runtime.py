#!/usr/bin/env python3

"""
program that measures the total execution time
for wait_n(n, max_delay), and returns total_time
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function that measures the total execution time
    for wait_n(n, max_delay), and returns total_time
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time: float = time.time() - start_time
    return elapsed_time / n
