#!/usr/bin/python3
"""This is a module to pass a Task
Here we define a class Square
"""


class Square:
    """This is an empty class
    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        """Validate if size is an integer
        It must also be superiour or qual to zero
        """
        self.size(self, size)

    def size(self):
        return self.__size

    def size(self, size):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size*self.__size
