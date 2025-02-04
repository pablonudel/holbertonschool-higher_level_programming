#!/usr/bin/python3
""" Duck Typing """
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """ Shape class """
    @abstractmethod
    def area(self):
        """ Area method """
        return 5

    @abstractmethod
    def Perimeter(self):
        """ Perimeter method """
        return 5


class Circle(Shape):
    """ Circle class """
    def __init__(self, radius):
        """ Circle constructor """
        self.radius = radius

    def area(self):
        """ Area method """
        return math.pi * self.radius ** 2

    def Perimeter(self):
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

    def Perimeter(self):
        """ Perimeter method """
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """ Shape info function """
    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.Perimeter()))
