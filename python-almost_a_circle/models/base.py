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

    @classmethod
    def to_json_string(cls, obj):
        """Converts to JSON string."""
        if obj is None:
            return None
        elif isinstance(obj, list):
            return json.dumps(obj)
        else:
            return json.dumps(obj.__dict__)

    @classmethod
    def from_json_string(cls, json_str=None, dictionary=None):
        """Creates an instance from a JSON string."""
        if json_str is not None:
            data = json.loads(json_str)
        elif dictionary is not None:
            data = dictionary
        else:
            return None

        if isinstance(data, list):
            return [cls(**item) for item in data]
        else:
            return cls(**data)

    @classmethod
    def saveToFile(cls, listObjs):
        """Saves to file."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            json.dump([cls.to_json_string(obj) for obj in listObjs], f)

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
