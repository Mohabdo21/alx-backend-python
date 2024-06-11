#!/usr/bin/env python3
"""
This module provides a coroutine for simulating random delays.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Pause for a random interval and return its duration.

    This coroutine pauses for a duration that is randomly chosen within
    the range [0, max_delay] and then returns that duration.

    Args:
        max_delay (Union[int, float]): The maximum delay duration in seconds.

    Returns:
        float: The actual delay duration in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
