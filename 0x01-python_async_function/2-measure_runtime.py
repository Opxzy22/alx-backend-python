#!/usr/bin/env python3

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measure_time: returns the average time taken to finish the process.

        Args:
            n (int): the number of times the function will run
            max_delay (int): the maximum time the function will sleep

        Returns:
            int: returns the average time.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = start_time - end_time

    return total_time / n
