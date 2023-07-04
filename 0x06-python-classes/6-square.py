#!/usr/bin/python3
"""This is a module to pass a Task
Here we define a class Square
"""


class Square:
    """This is an empty class
    Attributes:
        size (int): size of square
        position (:obj:`tuple`): position
    """
    def __init__(self, size=0, position=(0, 0)):
        """Validate if size is an integer
        It must also be superiour or qual to zero
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size*self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
