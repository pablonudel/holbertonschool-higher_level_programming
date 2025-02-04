#!/usr/bin/python3

from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        return super().append(item)

    def extend(self, item):
        if not isinstance(item, list):
            raise TypeError("Object is not iterable")
        print("Extended the list with [{}] items.".format(len(item)))
        return super().extend(item)

    def remove(self, item):
        if item not in self:
            raise ValueError("Item [{}] not found in the list".format(item))
        print("Removed [{}] from the list.".format(item))
        return super().remove(item)

    def pop(self, item=-1):
        if not (-len(self) <= item < len(self)):
            raise IndexError("index out of range")
        print("Popped [{}] from the list.".format(self[item]))
        return super().pop(item)
