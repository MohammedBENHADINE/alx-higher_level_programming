#!/usr/bin/python3
"""This is a module to pass a Task"""


class Rectangle:
    """Class rectangle with following attributes
    Attributes:
        width (int): width of rect
        height (int): height of rect
    """
    def __init__(self, width=0, height=0):
        """Init magic method"""
        self.height = height
        self.width = width

    @property
    """Getter method"""
    def height(self):
        return self.__height

    @property
    """Getter method"""
    def width(self):
        return self.__width

    @height.setter
    """Setter method"""
    def height(self, value):
        if type(value) != int:
            raise TypeError("heigtht must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    """Setter method"""
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
