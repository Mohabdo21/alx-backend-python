#!/usr/bin/env python3
"""
This module contains an asynchronous generator.
"""

import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields random numbers.

    This generator will loop 10 times, each time asynchronously
    waiting 1 second,
    then yielding a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
