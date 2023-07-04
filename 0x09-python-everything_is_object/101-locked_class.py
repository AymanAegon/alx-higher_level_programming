#!/usr/bin/python3
"""
101-locked_class Module
"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    """
    first_name = ''

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError("object has no attribute '{}'".format(name))
