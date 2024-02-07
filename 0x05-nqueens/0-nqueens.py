#!/usr/bin/python3
"""N Queens problems."""

import sys


def generate_solutions(n):
    """
    Solve N Queens problem for a given board size.
    Args:
        n (int): The size of the chessboard.
    Returns:
        List of solutions, each represented as a list of queen positions.
    """
    solutions = []
    solve(n, 0, [], solutions)
    return solutions


def solve(n, row, positions, solutions):
    """
    Backtracking function to find solutions for N Queens problem.
    Args:
        n (int): The size of the chessboard.
        row (int): Current row being processed.
        positions (list): Current positions of queens.
        solutions (list): List to store found solutions.
    Returns:
        None
    """
    if row == n:
        solutions.append(positions[:])
        return
    for col in range(n):
        if is_safe(row, col, positions):
            positions.append((row, col))
            solve(n, row + 1, positions, solutions)
            positions.pop()


def is_safe(row, col, positions):
    """
    Check if placing a queen at a given position is safe.
    Args:
        row (int): Row index of the position.
        col (int): Column index of the position.
        positions (list): Current positions of queens.
    Returns:
        bool: True if it's safe to place a queen at the position,
              False otherwise.
    """
    for queen_row, queen_col in positions:
        if queen_col == col or abs(queen_row - row) == abs(queen_col - col):
            return False
    return True


def main():
    """
    Main entry point of the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError("N must be at least 4")
    except ValueError as e:
        print("N must be a valid integer greater than or equal to 4")
        sys.exit(1)

    solutions = generate_solutions(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
