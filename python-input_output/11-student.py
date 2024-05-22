#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        if attrs is not None:
            dict_1 = {}
            for i in self.__dict__:
                if i in attrs:
                    dict_1[i] = self.__dict__[i]
            return dict_1
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        if json:
            self.__dict__ = json
