#!/usr/bin/python3
"""
MyInt Module
"""


class MyInt(int):
    """
    inherits from int
    """
    def __eq__(self, x):
        """
        invert to !=
        Args:
            x (int): other int
        """
        return super().__ne__(x)

    def __ne__(self, x):
        """
        invert to ==
        Args:
            x (int): other int
        """
        return super().__eq__(x)

