#!/usr/bin/env python3
"""
    Defines an async task_wait_n function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        wait_n: runs the task_wait_random function n times

        Args:
            n (int): the number of times the
            task_wait_random func will be called
            max_delay (int): the maximum time a func can be delayed

        Returns:
            List[float]: a list of all the delay times.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
