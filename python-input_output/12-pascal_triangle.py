#!/usr/bin/python3
"""Module for pascal_triangle method"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing Pascal's triangle of n."""
    if n <= 0:
        return []

    def create_row(prev_row):
        row = [1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        return row

    triangle = [[1]]
    for i in range(1, n):
        triangle.append(create_row(triangle[i - 1]))

    return triangle
