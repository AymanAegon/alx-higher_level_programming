#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) <= 0:
        return 0
    res = 0
    d = 0
    for e in my_list:
        d += e[1]
        res += e[0] * e[1]
    return res / d
