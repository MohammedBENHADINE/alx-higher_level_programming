#!/usr/bin/python3
"""
This a module's comment
"""


class MyList(list):
    """Class object of type MyList
    """
    def print_sorted(self):
        """Print the list in ascending mode
        """
        new = sorted(self)
        print(new)
