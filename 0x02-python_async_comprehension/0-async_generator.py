#!/usr/bin/env python3
"""
    async_generator coroutine function
"""
import random
import asyncio


async def async_generator():
    """
        async_generator: yields a randomly generated float.

    Returns:
        float: randomly generated float
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
