#!/usr/bin/python3
"""Student module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init module"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To json function"""
        return vars(self)
