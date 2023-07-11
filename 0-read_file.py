#!/usr/bin/python3
"""
Read file Module
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    f = open(filename, 'r', encoding="utf-8")
    print(f.read())
    f.close()
