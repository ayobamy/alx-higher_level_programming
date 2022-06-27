#!/usr/bin/python3
"""
 a class Rectangle that defines a
 rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    Private instance attribute: width
    Private instance attribute: height
    """
    def __init__(self, width=0, height=0):
        """Initializes the class"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self._height = value
