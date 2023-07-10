#!/usr/bin/python3
"""
is_same_class Module
"""


def is_same_class(obj, a_class):
    """
    Exact same object

    Args:
        obj (object): the object
        a_class (Class): the specified class
    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False.
    """
    return type(obj) is a_class
