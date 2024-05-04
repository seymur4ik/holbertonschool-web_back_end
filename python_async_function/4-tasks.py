#!/usr/bin/env python3
"""Module for function task_wait_random"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of tasks """
    tasks = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(tasks)
