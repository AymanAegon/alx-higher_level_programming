#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    Args:
        filename (str):
        text (str):

    Returns:
        the number of characters added
    """
    n = 0
    with open(filename, 'a', encoding="utf-8") as f:
        n = f.write(text)
    f.close()
    return n
