#!/usr/bin/python3
""" Duck Typing """
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """ Shape class """
    @abstractmethod
    def area(self):
        """ Area method """
        pass

    @abstractmethod
    def perimeter(self):
        """ Perimeter method """
        pass


class Circle(Shape):
    """ Circle class """
    def __init__(self, radius):
        """ Circle constructor """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self):
        """ Area method """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """ Perimeter method """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Rectangle constructor """
        if not all(isinstance(i, (int, float)) for i in [width, height]):
            raise TypeError("Width and height must be numbers")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self):
        """ Area method """
        return self.width * self.height

    def perimeter(self):
        """ Perimeter method """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ Shape info function """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
