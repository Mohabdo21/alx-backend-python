#!/usr/bin/env python3
"""
This module contains a coroutine that waits for a random delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Wait for a random delay and return the delay.

    This coroutine waits for a random delay between 0 and max_delay seconds
    and then returns the actual delay.

    Args:
        max_delay (Union[int, float]): The maximum delay in seconds.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
