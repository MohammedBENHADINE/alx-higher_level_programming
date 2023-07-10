#!/usr/bin/python3
"""
class module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Derived class"""

    def __init__(self, width, height):
        """init method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area of width and height"""
        return self.__width * self.__height

    def __str__(self):
        """print method"""
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)
