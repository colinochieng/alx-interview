#!/usr/bin/python3
"""
Module for Island Perimeter
"""


def island_perimeter(grid):
    """
    description: function that computes the
        perimeter of the island described in grid
    Args:
        grid: a list of list of integers
            -> 0 represents water
            -> 1 represents land
            -> Each cell is square, with a side length of 1
            -> Cells are connected horizontally/vertically (not diagonally).
            -> grid is rectangular, with its width and height not exceeding 100
            -> The grid is completely surrounded by water
            -> There is only one island (or nothing).
            -> The island doesn't have “lakes”
                (water inside that isn't connected to
                the water surrounding the island).
    return: perimeter of island
    """
    width = len(grid[0])
    height = len(grid)
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
