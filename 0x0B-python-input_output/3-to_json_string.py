#!/usr/bin/python3
"""
To JSON string Module
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj (object):

    Returns:
        the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
