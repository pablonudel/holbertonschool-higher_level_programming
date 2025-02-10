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
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            reversed_attrs = attrs[::-1]
            return {
                key: getattr(self, key)
                for key in reversed_attrs
                if hasattr(self, key)
            }
        else:
            reversed_dict_keys = list(self.__dict__.keys())[::-1]
            return {key: self.__dict__[key] for key in reversed_dict_keys}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in self.__dict__:
            setattr(self, key, json[key])
