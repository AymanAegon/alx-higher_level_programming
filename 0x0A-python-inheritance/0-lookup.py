#!/usr/bin/python3
"""
Lookup Module
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object

    Returns:
        the list
    """
    return dir(obj)
