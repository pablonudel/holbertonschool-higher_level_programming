#!/usr/bin/python3
""" Module for the BaseGeometry class """


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Method that raises an Exception"""
        if self:
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
