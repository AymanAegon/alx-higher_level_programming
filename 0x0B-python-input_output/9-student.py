#!/usr/bin/python3
"""
Student to JSON Module
"""


class Student:
    """
    Student class implementation

        Methods:
            to_json(): retrieves a dictionary representation of a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        inistializes a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student
        """
        return self.__dict__
