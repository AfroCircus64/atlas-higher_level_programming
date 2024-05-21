#!/usr/bin/python3
"""Defines the class to inherit the list"""


class MyList(list):
    """class that defines the print_sorted func"""
    pass

    def print_sorted(self):
        """function to sort the list (ascending order)"""
        print(sorted(list(self)))
