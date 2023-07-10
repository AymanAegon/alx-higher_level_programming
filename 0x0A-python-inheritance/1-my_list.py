#!/usr/bin/python3
"""
MyList class Module
"""


class MyList(list):
    """
    MyList implementation

    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """
        prints the list, but sorted
        """
        print(sorted(self))
