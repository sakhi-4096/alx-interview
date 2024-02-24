#!/usr/bin/python3
"""This module provides a function to rotate an m by n 2D matrix in place.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.

    Args:
        matrix (list): The 2D matrix to rotate.
    Returns:
        None: The matrix is rotated in place. No explicit return value.
    """
    # Check if the input is a valid list of lists
    if not isinstance(matrix, list) or not matrix:
        return

    # Check if all elements are lists and have consistent lengths
    if (not all(isinstance(row, list) for row in matrix) or
            not all(len(row) == len(matrix[0]) for row in matrix)):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    # Rotate layer by layer
    for layer in range(rows // 2):
        first = layer
        last = rows - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
