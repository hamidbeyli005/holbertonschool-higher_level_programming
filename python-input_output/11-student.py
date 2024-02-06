#!/usr/bin/python3
"""Student module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init module"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json function"""
        if attrs is None:
            return vars(self)
        else:
            r = {x: getattr(self, x) for x in attrs if hasattr(self, x)}
            return r
    def reload_from_json(self, json):
        """Reload from json"""
        for key, value in json.items():
            setattr(self, key, value)
