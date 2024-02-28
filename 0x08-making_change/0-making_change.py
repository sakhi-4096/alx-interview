#!/usr/bin/python3
"""
This module provides a function to determine the minimum number of coins
required to make a certain total value using a given set of coin
denominations.

Functions:
    makeChange(coins, total): Determine the minimum number of coins required
    to make the total.
"""

def makeChange(coins, total):
    """
    Determine the minimum number of coins required to make the given total.

    Args:
        coins (list of int): List of coin denominations available.
        total (int): Total value to make using the coins.
    Returns:
        int: Minimum number of coins required to reach the total.
             Returns -1 if it's not possible to make the total using the given
             coins.
    """
    if total <= 0:
        return 0

    # Create an array to store the minimum number of coins required to reach
    # each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update the minimum number of coins required for each value
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins required to reach the total value
    return min_coins[total] if min_coins[total] != float('inf') else -1
