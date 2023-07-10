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
        super().integer_validator("width", height)
        self.__width = width
        self.__height = height
