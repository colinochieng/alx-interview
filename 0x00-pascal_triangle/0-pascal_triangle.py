#!/usr/bin/python3
"""
Module for a function that generates a 2D array
resembling Pascal's Triangle
"""


def pascal_triangle(n):
    """
    descritption: a function that formats
        a 2D list of Pascal's Triangle
    Args:
        n (int): assuming n will be always an integer
            this determine the extent of the triangle
    Return: empty list if n <= 0 or 2D list
    """
    if n <= 0:
        return []
    else:
        pascal_2D = [[1]]

        if n == 1:
            return pascal_2D

        def create_list_of_zeros(a):
            """
            create a list of zeros
            Args: a (int): determines length of new list
            """
            return [0] * a

        for value in range(2, n + 1):
            new_list = create_list_of_zeros(value)
            new_list[0], new_list[value - 1] = (1, 1)

            idx_new_list = 1

            # value is always greater than length of pascal_2D by 1
            prev_list = pascal_2D[value - 2]
            idx_prev_list = 0

            while idx_new_list < value - 1:
                tmp = prev_list[idx_prev_list] + prev_list[idx_prev_list + 1]
                new_list[idx_new_list] = tmp
                idx_new_list += 1
                idx_prev_list += 1

            pascal_2D.append(new_list)

        return pascal_2D
