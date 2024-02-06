#!/usr/bin/python3
"""Load from json file module"""


import json


def load_from_json_file(filename):
    """load from json file function"""
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
