#!/usr/bin/env python3
"""
This module contains an asynchronous function that executes `task_wait_random`
multiple times concurrently.

The function, `task_wait_n`, concurrently executes `task_wait_random` for a
specified number of times and returns the delays in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times."""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
