#!/usr/bin/python3
"""
Search and update Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    s = ""
    with open(filename, 'r+', encoding="utf-8") as f:
        while True:
            line = f.readline()
            s += line
            if line == '':
                break
            if search_string in line:
                s += new_string
        f.seek(0)
        f.truncate()
        f.write(s)

    f.close()
