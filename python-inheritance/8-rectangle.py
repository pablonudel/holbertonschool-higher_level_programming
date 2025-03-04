#!/usr/bin/python3
""" Module for the BaseGeometry class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Method that initializes the rectangle """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
