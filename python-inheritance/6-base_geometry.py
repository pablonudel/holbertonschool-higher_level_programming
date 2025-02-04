#!/usr/bin/python3
""" Module for the BaseGeometry class """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ Method that raises an Exception with the message """
        if self:
            raise Exception("area() is not implemented")
