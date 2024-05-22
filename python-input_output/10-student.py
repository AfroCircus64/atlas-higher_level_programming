#!/usr/bin/python3
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
            return self.__dict__
        dict_1 = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dict_1[key] = value
        return dict_1
