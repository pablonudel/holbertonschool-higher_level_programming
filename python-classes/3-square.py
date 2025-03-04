#!/usr/bin/python3
""" This module creates a Square Class """


class Square:
    """ Square class with size validation and area method """
    __size = None

    def area(self):
        return self.__size ** 2

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
