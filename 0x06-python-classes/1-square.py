#!/usr/bin/python3
"""
class Square defines a square
"""


class Square:
    """
    class Square definition

    Attributes:
        __size (float): size of a side in square
    """
    __size = 0
    def __init__(self, size = 0):
        """
        Initializes a square

        Args:
            size (float): size of a side in square
        """
        self.__size = size
