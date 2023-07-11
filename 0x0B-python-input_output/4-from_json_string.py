#!/usr/bin/python3
"""
From JSON string to Object Module
"""


import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (object):

    Returns:
        an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
