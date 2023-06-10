#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for n in my_list:
        if n % 2:
            res.append(False)
        else:
            res.append(True)

    return res
