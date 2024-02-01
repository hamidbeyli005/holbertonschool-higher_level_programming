#!/usr/bin/python3
"""
2-matrix_divided

This module provides a function for dividing each
element of a matrix by a given divisor.

"""


def matrix_divided(matrix, div):
    """
    Divide each element of the matrix by the specified divisor.

    Parameters:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix where each element
        is the result of the division rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a valid matrix (list of lists)
                    of integers/floats,or if each row of the matrix
                    does not have the same size.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    list_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(list_error)
    length = len(matrix[0])
    if any(len(row) != length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix
