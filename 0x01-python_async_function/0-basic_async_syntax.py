#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random
import time


@asyncio.coroutine
def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    time.sleep(wait_time)
    return wait_time
