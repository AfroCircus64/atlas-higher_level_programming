#!/usr/bin/python3
"""Defines a func - append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""

    with open(filename, mode='a', encoding='utf-8') as writer:
        return writer.write(text)
