#!/usr/bin/python3
"""
Defines the base model for geometric shapes.
"""

import json


class Base:
    """
    Base class for managing geometric shapes.

    Attributes:
        __nb_objects (int): Number of Base instances created.
        id (int): Unique identifier for each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """make json file"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns from json file"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes from json str to file"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list)
            f.write(json_string)

    @classmethod
    def loadFromFile(cls):
        """Loads from file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                objs_data = json.load(f)
                return [cls.from_json_string(data) for data in objs_data]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **kwargs):
        """Creates an instance with all attributes already set."""
        dummy_instance = cls(**{k: v for k, v in kwargs.items()})
        dummy_instance.update(**kwargs)
        return dummy_instance
