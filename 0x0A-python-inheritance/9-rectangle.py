#!/usr/bin/python3
"""
A subclass definition of class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a subclass of the Super class BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height:
        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = width

    def area(self):
        """
        the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print() and str() representation of a Rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
