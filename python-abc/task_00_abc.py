#!/usr/bin/python3
""" Abstract Base Class """
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Animal class """
    @abstractmethod
    def sound(self):
        """ Sound method """
        pass


class Dog(Animal):
    """ Dog class """
    def sound(self):
        """ Sound method """
        return "Bark"


class Cat(Animal):
    """ Cat class """
    def sound(self):
        """ Sound method """
        return "Meow"
