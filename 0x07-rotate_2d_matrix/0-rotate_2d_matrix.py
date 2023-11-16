#!/usr/bin/python3
"""
Module to for rotating 2D Matrix
"""
from typing import List, Union


def rotate_2d_matrix(matrix: List[List[Union[int, float, str]]]) -> None:
    """
    describe: function to rotate 2D matrix 90 degrees clockwise
        given an n x n 2D matrix
    param:
        matrix: n x n 2D List
    return: nothing. The matrix must be edited in-place
    assumption: assume the matrix will have
        2 dimensions and will not be empty
    """
    # step1: shift columns to rows

    new_matrix = [list(row) for row in zip(*matrix)]

    # step2: reverse rows of new matrix
    idx = 0

    for row in new_matrix:
        matrix[idx] = list(reversed(row))
        idx += 1
