#!/usr/bin/python3

import json

class Base:
    _instances = []

    def __init__(self):
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
    def from_json_string(cls, json_str):
        if json_str is None:
            return None
        elif json_str == "[]":
            return []
        else:
            return cls(**json.loads(json_str))
