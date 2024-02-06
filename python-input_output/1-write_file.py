#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Write file function"""
    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
