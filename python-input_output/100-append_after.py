#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """append after functon"""
    text = ''
    with open(filename, encoding='utf-8') as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(text)
