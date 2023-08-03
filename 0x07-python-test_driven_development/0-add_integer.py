#!/usr/bin/python3
"""
    Add two integers
"""


def add_integer(a, b=98):
    """
    This method checks if both variables are int/float.
    """
    res = 0

    if a is None or (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        res += int(a)
    else:
        res += a
    if type(b) is float:
        res += int(b)
    else:
        res += b
    return res