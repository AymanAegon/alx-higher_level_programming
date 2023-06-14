#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def fun(arr=[]):
        return list(map(lambda x: x * x, arr))
    return list(map(lambda arr: fun(arr), matrix))
