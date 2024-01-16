#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
        float: Random delay.
    """
    i = random.uniform(0, 10)
    await asyncio.sleep(i)
    return i
