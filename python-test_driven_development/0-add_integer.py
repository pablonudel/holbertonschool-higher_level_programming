#!/usr/bin/python3
"""
This module provides a function to add two numbers
after validating their types. It ensures inputs are integers
or floats before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating their types.
    Returns the result as integer.
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a + b)
