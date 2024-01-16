#!/usr/bin/env python3
"""
    Defines the task_wait_random function
"""
import asyncio
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
        task_wait_random: return an asyncio.Task generated from wait_random

        Args:
            max_delay (int): the maximum number the async function will sleep

        Returns:
            IO: an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
