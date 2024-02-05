#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """check if obj isinstance of a_class that inherited
    Args:
        obj: the object
        a_class: the class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
