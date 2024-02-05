#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList, inherits from list"""
    def print_sorted(self):
        """print sorted list method"""
        print(sorted(self))
