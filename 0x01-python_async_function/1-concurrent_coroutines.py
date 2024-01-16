#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    delay = []

    task = [wait_random(max_delay) for _ in range(n)]

    for completed_task in asyncio.as_completed(task):
        value = await completed_task
        delay.append(value)
    return delay
