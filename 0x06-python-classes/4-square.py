#!/usr/bin/python3
"""
Module 3-square
Defines class Square with Size validation
"""


class Square:
    """
    class Square definition

    Args:
        size: size of a side in square

    Methods:
        area(): returns the current square area
        size(): gets the attribute size
        size(value): sets attribute size to a square
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size: size of a side of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """
        returns the current square area

        Returns:
            the current square area
        """
        return self.__size ** 2
    @property
    def size(self):
        """
        gets the attribute size

        Returns: size
        """

        return self.__size
    @size.setter
    def size(self, value):
        """
        sets attribute size to a square

        Attributes:
            value: new size of a side of square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
