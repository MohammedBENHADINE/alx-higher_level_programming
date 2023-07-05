#!/usr/bin/python3
"""Module to pass Task"""


class LockedClass:
    """class that prevents the user from
    dynamically creating new instance att
    """
    __slots__ = ['first_name']
