#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = []
    for n in my_list:
        if search == n:
            a.append(replace)
        else:
            a.append(n)
    return a
