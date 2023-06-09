#!/usr/bin/python3
"""
MyInt Module
"""


class MyInt(int):
    """
    inherits from int

    Methods:
        __eq__(self, x):
        __ne__(self, x):
    """

    def __eq__(self, x):
        """
        invert to !=

        Args:
            x (int): other int

        Return:
            self != x
        """
        return super().__ne__(x)

    def __ne__(self, x):
        """
        invert to ==

        Args:
            x (int): other int

        Return:
            self == x
        """
        return super().__eq__(x)
