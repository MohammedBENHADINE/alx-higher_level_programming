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
        self.__size = 0  # init before
        self.size = size  # call to a local prperty

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size*self.__size
