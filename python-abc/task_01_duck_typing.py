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
    if not isinstance(shape, Shape):
        raise TypeError("Provided object is not a Shape instance")
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
