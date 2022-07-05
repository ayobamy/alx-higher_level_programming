#!/usr/bin/python3
"""
a definition of a class BaseGeometry
"""


class BaseGeometry:
    """A class definition"""

    def area(self):
        """
        raises an Exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value:

        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer

        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
A subclass of class BaseGeometry
"""


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
