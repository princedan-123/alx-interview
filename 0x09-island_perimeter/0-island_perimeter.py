#!/usr/bin/python3
"""A script that solves the island perimeter grid problem."""


def island_perimeter(grid):
    """
    A function that calculates the perimiter of an island grid.
    args:   grid(list) A 2-d list representing an island.
    return: integer representing the perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
