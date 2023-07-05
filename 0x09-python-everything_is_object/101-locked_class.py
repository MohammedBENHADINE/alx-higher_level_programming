#!/usr/bin/python3
"""Module to pass Task"""


class LockedClass:
    """class that prevents the user from
    dynamically creating new instance att
    """
    def __setattr__(self, name, value):
        """Magic class"""
        if not hasattr(self, name) or name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'"
                    .format(name)
                    )
