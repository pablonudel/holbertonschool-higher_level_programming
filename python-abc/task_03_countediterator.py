#!/usr/bin/python3

class CountedIterator():
    def __init__(self, object):
        if not hasattr(object, '__iter__'):
            raise TypeError
        self.iterator = iter(object)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        if not item:
            raise StopIteration
        self.counter += 1
        return item
