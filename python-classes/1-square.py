#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=__size):
        if size is not None:
            self.__size = size
