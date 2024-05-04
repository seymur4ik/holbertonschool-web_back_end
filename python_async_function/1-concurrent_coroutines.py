#!/usr/bin/env python3
""" Concurrent coroutines """
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays
    """
    list_of_delays = []
    for i in range(n):
        list_of_delays.append(await wait_random(max_delay))
    return sorted(list_of_delays)
