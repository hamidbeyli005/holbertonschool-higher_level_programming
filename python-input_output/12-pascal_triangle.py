#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """pascal function"""
    if n <= 0:
        return []
    length = n + 1
    for i in range(n):
        for j in range(i - length):
            print(j)
        print()
