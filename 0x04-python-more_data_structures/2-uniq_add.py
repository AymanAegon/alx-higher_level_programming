#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = []
    for n in my_list:
        if n not in a:
            a.append(n)
    sum = 0
    for n in a:
        sum += n
    return sum
