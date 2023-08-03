#!/usr/bin/python3
"""
    divide matrix by an integer
"""


def matrix_divided(matrix, div):
    """
    divide matrix elements by div
    while making sure types are correct
    """
    base = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != base:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    newmatrix = [[round(x/div, 2) for x in row] for row in matrix]
    return newmatrix
