#!/usr/bin/python3
"""Is same class module"""


def is_same_class(obj, a_class):
    """check if object is exactly and instance of given class
    Args:
        obj: the object we're checking
        a_class: the class we are checking for
    """
    return type(obj) is a_class
