#!/usr/bin/python3
"""
This module defines a function that calculates the minimum operations
required to copy and paste letters.
"""


def min_operations(n):
    """
    Calculate the minimum operations to copy and paste letters.

    Parameters:
        n (int): The number of letters to be copied.
    Returns:
        int: The minimum operations required.
    """
    nOpe = 0  # Variable to track the number of operations
    minOpe = 2  # Starting from 2 as the minimum possible operation

    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1

    return nOpe
