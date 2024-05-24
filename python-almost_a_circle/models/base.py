#!/usr/bin/python3

import json


class Base:
    _instances = []

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = len(self._instances)
        self._instances.append(self)

    @classmethod
    def to_json_string(cls, obj):
        if obj is None:
            return None
        elif isinstance(obj, list):
            return json.dumps(obj)
        else:
            return json.dumps(obj.__dict__)

    @classmethod
    def from_json_string(cls, json_str=None, dictionary=None):
        if json_str is not None:
            data = json.loads(json_str)
            if isinstance(data, list):
                return [cls(**item) for item in data]
            else:
                return cls(**data)
        elif dictionary is not None:
            return cls(**dictionary)
        else:
            return None

    @classmethod
    def saveToFile(cls, listObjs):
        with open('objects.json', 'w') as f:
            json.dump([cls.to_json_string(obj) for obj in listObjs], f)

    @classmethod
    def loadFromFile(cls):
        try:
            with open('objects.json', 'r') as f:
                objs_data = json.load(f)
            return [cls.from_json_string(data) for data in objs_data]
        except FileNotFoundError:
            return []
