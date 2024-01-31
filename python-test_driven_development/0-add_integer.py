#!/usr/bin/python3
"""This module contains a function that returns
    the addition of two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a: the first int
        b: the second int, default 98.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
