#!/usr/bin/python3
"""This a module's comment"""
def lookup(obj):
    """Return a list of attributes of a class"""
    res = []
    for attr in dir(obj):
        res.append(getattr(obj, attr))
    return res
