#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
The matrix must be a list of lists of integers or floats.
Each row of the matrix must be of the same size.
"div" must be a number (integer or float) but not 0.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by "div".
    Returns a new matrix with results rounded to 2 decimal places.
    """
    te_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError(te_msg)
        for i in row:
            row_len = len(row)
            if isinstance(i, (int, float)) is False:
                raise TypeError(te_msg)
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
