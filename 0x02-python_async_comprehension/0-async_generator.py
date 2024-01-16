#!/usr/bin/env python3
"""
    async_generator coroutine function
"""
import random
import asyncio


async def async_generator():
    """
    async generator that run a loop 10 times
    For each iteration:
    - wait for 1 second
    - yields a random float number between 0 and 10 using random.uniform
    
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1) 
