#!/usr/bin/env python3
"""
    measure_runtime coroutine function
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    for i in range(4):
        start_time = time.perf_counter()
        await asyncio.gather(async_comprehension())
        end_time = time.perf_counter()
        result = end_time - start_time

        return result
