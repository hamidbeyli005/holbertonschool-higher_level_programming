#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """pascal function"""
    if n <= 0:
        return []
    matrix = []

    for i in range(n):
        row = str(11 ** i)
        matrix.append(row)
    return matrix
