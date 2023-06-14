#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    a = []
    for arr in matrix:
        for n in arr:
            a.append(n * n)
        new_matrix.append(a)
        a = []
    return new_matrix
