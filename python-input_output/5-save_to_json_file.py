#!/usr/bin/python3
"""Defines a func - save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file as a JSON"""

    with open(filename, mode='w', encoding='utf-8') as writer:
        json.dump(my_obj, writer)
