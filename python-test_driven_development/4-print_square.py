#!/usr/bin/python3
"""
This module provides a function that prints a square with the character #
<size> is the size length of the square
and must be a positive integer
"""


def print_square(size):
    """
    function that prints a square with the character #
    with length of <size>
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    row = 0
    while row < size:
        col = 0
        while col < size:
            col += 1
            print('#', end='')
        row += 1
        print()
