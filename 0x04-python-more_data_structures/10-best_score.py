#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) <= 0:
        return None
    a = list(a_dictionary.keys())
    max = a[0]
    for n in a:
        if a_dictionary[n] > a_dictionary[max]:
            max = n
    return max
