#!/usr/bin/env python3
"""
    async_comprehension coroutine function
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using an
    async comprehension over async_generator.
    """
    result = [i async for i in async_generator()]
    return result
