#!/usr/bin/python3
"""
Module for defining change generating function
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    describe: Given a pile of coins of different values,
        the function determines the fewest number of coins
        needed to meet a given amount total.
    params:
        coins: a list of different values of coins
        total: amount to return]
    returns:
        - fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total is 0 or less, return 0
    """
    if total <= 0:
        return 0

    coin_count = 0
    while len(coins) > 0:
        maxValue = max(coins)

        while maxValue <= total:
            total = total - maxValue
            coin_count += 1

        coins.remove(maxValue)
        if total == 0:
            break

    return coin_count if total == 0 else -1
