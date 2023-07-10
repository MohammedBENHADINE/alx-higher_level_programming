#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __eq__(self, other):
        """equal equal method"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """not equal method"""
        return not super().__ne__(other)
