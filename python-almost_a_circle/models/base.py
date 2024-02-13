#!/usr/bin/python3
"""Base class module"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To json string method"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ from json string method"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load from file"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as my_file:
                data = cls.from_json_string(my_file.read())
            instances = []
            for i in data:
                instances.append(cls.create(**i))
            return instances
        except IOError:
            return []
