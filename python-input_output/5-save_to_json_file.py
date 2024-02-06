#!/usr/bin/python3
"""Dave to json file module"""


import json


def save_to_json_file(my_obj, filename):
    """Save to json function"""
    with open(filename, 'w', encoding="utf-8") as myFile:
        return json.dump(my_obj, myFile)
