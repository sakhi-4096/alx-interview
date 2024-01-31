#!/usr/bin/python3
"""UTF-8 validation module."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Checks if a list of integers are valid UTF-8 code points.

    Args:
        data (List[int]): List of integers representing UTF-8 code points.
    Returns:
        bool: True if the list represents valid UTF-8 code points,
              False otherwise.
    """
    # Helper function to check if the next bytes are valid continuation bytes
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    n = len(data)

    while i < n:
        current_byte = data[i]

        # Check for single-byte character (ASCII)
        if current_byte <= 0x7f:
            i += 1

        # Check for multi-byte character encoding
        elif (current_byte & 0b11111000) == 0b11110000:
            span = 4
            if i + span <= n and (all(is_continuation(data[j])
                                  for j in range(i + 1, i + span))):
                i += span
            else:
                return False

        elif (current_byte & 0b11110000) == 0b11100000:
            span = 3
            if i + span <= n and (all(is_continuation(data[j])
                                  for j in range(i + 1, i + span))):
                i += span
            else:
                return False

        elif (current_byte & 0b11100000) == 0b11000000:
            span = 2
            if i + span <= n and (all(is_continuation(data[j])
                                  for j in range(i + 1, i + span))):
                i += span
            else:
                return False

        else:
            return False

    return True
