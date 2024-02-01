#!/usr/bin/python3
def matrix_divided(matrix, div):
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
