#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res1 = tuple_a[0] if len(tuple_a) > 0 else 0
    res1 += tuple_b[0] if len(tuple_b) > 0 else 0

    res2 = tuple_a[1] if len(tuple_a) > 1 else 0
    res2 += tuple_b[1] if len(tuple_b) > 1 else 0

    t = (res1, res2)
    return t
