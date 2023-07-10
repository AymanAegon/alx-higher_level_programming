#!/usr/bin/python3
"""
Rectangle Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry

    Methods:
        area(self)
    """
    def __init__(self, width, height):
        """
        initializes a Rectangle

        Args:
            width (int):
            height (int):
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate the area

        Returns:
            area result
        """
        return self.__width * self.__height

    def __str__(self):
        """
        return following rectangle description:
        [Rectangle] <width>/<height>

        Returns:
            [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
