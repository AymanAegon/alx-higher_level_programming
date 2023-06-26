#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except ZeroDivisionError as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
    except IndexError as ex2:
        print("Exception: {}".format(ex2), file=sys.stderr)

    return result
