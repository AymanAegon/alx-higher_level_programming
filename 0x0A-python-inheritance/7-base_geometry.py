#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:
    """
    BaseGeometry implementation

    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name (String):
            value (int):
        """
        if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
