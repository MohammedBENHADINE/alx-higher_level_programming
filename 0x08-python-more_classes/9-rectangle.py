#!/usr/bin/python3
"""This is a module to pass a Task"""


class Rectangle:
    """Class rectangle with following attributes
    Attributes:
        width (int): width of rect
        height (int): height of rect
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init magic method"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """class method"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @height.setter
    def height(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Get area of rect"""
        return self.__width * self.__height

    def perimeter(self):
        """Get perimeter of rect"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """magic method"""
        if (self.__width == 0 or self.__height == 0):
            return ""
        res = ""
        for _ in range(self.__height):
            res += str(self.print_symbol) * self.__width + '\n'
        return res.rstrip()

    def __repr__(self):
        """Magic method fallback"""
        return "Rectangle(" + str(self.__width) + ", " \
                + str(self.__height) + ")"

    def __del__(self):
        """magic method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
