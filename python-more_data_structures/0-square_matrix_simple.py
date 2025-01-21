#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row in new_matrix:
        for i in range(len(row)):
            row[i] = row[i] ** 2
    return new_matrix
