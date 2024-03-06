#!/usr/bin/python3
'''
Calculate and return the perimeter of the island in the given grid.
'''


def island_perimeter(grid):
    '''
    This function traverses the grid and calculates the perimeter of the
    island. It iterates over each cell in the grid. If the cell represents
    land (1), it adds 4 to the perimeter. Then, it checks adjacent cells
    to reduce the perimeter if there is land neighboring the current cell.

    Args:
    grid (List[List[int]]): A 2D grid representing the island.
    Returns:
    int: The perimeter of the island.
    '''
    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
