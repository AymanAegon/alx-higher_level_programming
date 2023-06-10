#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        if len(a) < 1:
            print()
        else:
            print("{:d}".format(a[0]), end='')
            for n in a[1:]:
                print(" {:d}".format(n), end='')
            print()
