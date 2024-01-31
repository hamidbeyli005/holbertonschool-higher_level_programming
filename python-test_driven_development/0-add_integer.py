#!/usr/bin/python3
"""
Module to sum
add_integer: adds two integers and return

"""


def add_integer(a, b=98):

    """Adds two integers.
    Args: a = int/float b = int/float
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
