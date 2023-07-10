#!/usr/bin/python3
"""
Rectangle Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
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
