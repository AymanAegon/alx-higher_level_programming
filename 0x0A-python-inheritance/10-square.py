#!/usr/bin/python3
"""
Square Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle
    """
    def __init__(self, size):
        """
        initializes a square

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculate the area

        Returns:
            area result
        """
        return self.__size * self.__size

    def __str__(self):
        """
        return following rectangle description:
        [Rectangle] <width>/<height>

        Returns:
            [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
