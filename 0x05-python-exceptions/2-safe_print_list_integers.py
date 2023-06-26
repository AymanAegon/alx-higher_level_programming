#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    l = 0
    while i < x:
        try:
            n = my_list[i]
        except IndexError:
            break
        i += 1
        try:
            print("{:d}".format(n), end="")
        except Exception:
            continue
        l += 1
    print()
    return l
