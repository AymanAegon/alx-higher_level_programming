#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = []
    for n in my_list:
        a.append(n)
    if idx < 0 or idx >= len(my_list):
        return a
    a[idx] = element
    return a
