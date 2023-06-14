#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = set()
    for e in set_1.difference(set_2):
        a.add(e)
    for e in set_2.difference(set_1):
        a.add(e)
    return a
