#!/usr/bin/python3
"""
add_attribute Module
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible

    Args:
        name (string): name of the attribute
        value (): the value

    """
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
