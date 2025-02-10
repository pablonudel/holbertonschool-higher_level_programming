#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return {key: self.__dict__[key] for key in sorted(self.__dict__)}
        new_dict = {}
        for key in sorted(attrs):
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in self.__dict__:
            setattr(self, key, json[key])
