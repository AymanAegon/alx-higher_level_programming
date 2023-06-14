#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            a.append(key)
    for key in a:
        a_dictionary.pop(key)
    return a_dictionary
