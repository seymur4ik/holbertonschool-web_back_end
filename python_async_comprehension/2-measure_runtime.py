#!/usr/bin/env python3
"""Measure runtime"""

import asyncio
import time
from typing import Generator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start = time.time()
    async_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*async_list)
    end = time.time()
    return end - start
