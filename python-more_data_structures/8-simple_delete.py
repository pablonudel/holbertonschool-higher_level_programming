#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in list(a_dictionary.keys()):
        if i == key:
            del a_dictionary[i]
    return a_dictionary
