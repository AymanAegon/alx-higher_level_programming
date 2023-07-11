#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)

    Args:
        filename (str):
        text (str):

    Returns:
        the number of characters written
    """
    n = 0
    with open(filename, 'w', encoding="utf-8") as f:
        n = f.write(text)
    f.close()
    return n
