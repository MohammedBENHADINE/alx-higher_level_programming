#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __ee__(self, other):
        """equal equal method"""
        return not super().__ee__(other)

    def __ne__(self, other):
        """not equal method"""
        return not super().__ne__(other)
