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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
