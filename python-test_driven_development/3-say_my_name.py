#!/usr/bin/python3
"""
my_name_module

This module provides a function for printing a formatted name.

"""


def say_my_name(first_name, last_name=""):
    """
        Print a formatted name.

        Parameters:
            first_name (str): The first name.
            last_name (str): The last name. Defaults to an empty string.

        Raises:
            TypeError: If first_name is not a string.
            TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
