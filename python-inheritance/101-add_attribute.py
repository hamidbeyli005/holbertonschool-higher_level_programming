#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, field, value):
    """Add attribute method"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, field, value)
