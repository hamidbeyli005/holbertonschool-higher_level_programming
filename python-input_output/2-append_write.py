#!/usr/bin/python3
"""Appen write module"""


def append_write(filename="", text=""):
    """append write function"""
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
