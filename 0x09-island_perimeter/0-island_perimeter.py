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
    # strip: a row of land``
    perimeter = 0

    for index, strip in enumerate(grid):
        # grid is completely surrounded by water (remove outside rows)
        if index > 0 and index < len(grid) - 1:
            for idx, unit in enumerate(strip):
                prev_strip = grid[index - 1]
                next_strip = grid[index + 1]

                # grid is completely surrounded by water
                # (remove outside columns)
                if idx > 0 and idx < len(strip) - 1:
                    if (unit == 1 and strip[idx - 1] == 0
                            and strip[idx + 1] == 0):
                        # prev and next strip
                        if prev_strip[idx] == 0 and next_strip[idx] == 0:
                            # island with one sq grid
                            return 4

                        elif prev_strip[idx] == 1 and next_strip[idx] == 0:
                            perimeter += 3

                        elif prev_strip[idx] == 0 and next_strip[idx] == 1:
                            perimeter += 3

                        elif prev_strip[idx] == 1 and next_strip[idx] == 1:
                            perimeter += 2

                    elif (unit == 1 and strip[idx - 1] == 1
                            and strip[idx + 1] == 0):
                        # prev and next strip
                        if prev_strip[idx] == 0 and next_strip[idx] == 0:
                            perimeter += 3

                        elif prev_strip[idx] == 1 and next_strip[idx] == 0:
                            perimeter += 2

                        elif prev_strip[idx] == 0 and next_strip[idx] == 1:
                            perimeter += 2

                        elif prev_strip[idx] == 1 and next_strip[idx] == 1:
                            perimeter += 1

                    elif (unit == 1 and strip[idx - 1] == 0
                            and strip[idx + 1] == 1):
                        # prev and next strip
                        if prev_strip[idx] == 0 and next_strip[idx] == 0:
                            perimeter += 3

                        elif prev_strip[idx] == 1 and next_strip[idx] == 0:
                            perimeter += 2

                        elif prev_strip[idx] == 0 and next_strip[idx] == 1:
                            perimeter += 2

                        elif prev_strip[idx] == 1 and next_strip[idx] == 1:
                            perimeter += 1

                    elif (unit == 1 and strip[idx - 1] == 1
                            and strip[idx + 1] == 1):
                        # prev and next strip
                        if prev_strip[idx] == 0 and next_strip[idx] == 0:
                            perimeter += 2

                        elif prev_strip[idx] == 1 and next_strip[idx] == 0:
                            perimeter += 1

                        elif prev_strip[idx] == 0 and next_strip[idx] == 1:
                            perimeter += 1

                        else:
                            # enclosed cell: no perimeter to sum up
                            continue
    return perimeter
