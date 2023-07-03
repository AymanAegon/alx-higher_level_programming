#!/usr/bin/python3

"""
A module with a Rectangle that does nothing
"""


class Rectangle:
    """
    An empty Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height

        Args:
            width (int): the width of Rectangle
            height (int): the height of Rectangle

        Raises:
            TypeError: If `width/height` type is not `int`.
            ValueError: If `width/height` is less than `0`.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        checks and sets the width

        Args:
            value (int): the new width value

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        checks and sets the height

        Args:
            value (int): the new height value

        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height
