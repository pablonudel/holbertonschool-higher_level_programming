#!/usr/bin/python3
"""Module for CustomObject class"""
import pickle


class CustomObject:
    """CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print out the attributes of the object"""
        for key in self.__dict__:
            print("{}: {}".format(key.capitalize(), self.__dict__[key]))

    def serialize(self, filename):
        """serialize the current instance of the object
        and save it to the provided filename"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError) as e:
            print("Serialization error: {}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """load and return an instance of the CustomObject
        from the provided filename"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if not isinstance(obj, cls):
                    raise TypeError("Object is not of type CustomObject")
                return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print("Deserialization error: {}".format(e))
            return None
