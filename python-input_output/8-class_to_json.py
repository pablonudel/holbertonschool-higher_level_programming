#!/usr/bin/python3
"""Module for class_to_json method"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
