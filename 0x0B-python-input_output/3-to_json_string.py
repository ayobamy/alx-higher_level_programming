#!/usr/bin/python3
import json
"""
 a function that returns the JSON
 representation of an object (string)
"""


def to_json_string(my_obj):
    """
    JSON representation of an object
    """
    json_rep = json.dumps(my_obj)
    return json_rep
