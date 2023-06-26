#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except ZeroDivisionError:
        print("Exception: division by 0", sys.stderr)
    except IndexError:
        print("Exception: list index out of range", sys.stderr)

    return result
