#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            n = my_list[i]
        except IndexError:
            break
        try:
            print("{:d}".format(n), end="")
            printed += 1
        except Exception:
            continue
    print()
    return printed
