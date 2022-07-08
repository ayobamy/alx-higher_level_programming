#!/usr/bin/python3
"""
Inherits from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defining a Rectangle class
    private instance attributes:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initisalizing class
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Set/get width of the Rectangle
        """
        return self.width

    @property
    def height(self):
        """
        Set/get height of the Rectangle
        """
        return self.height

    @property
    def x(self):
        """
        Set/get x value of the Rectangle
        """
        return self.x

    @property
    def y(self):
        """
        Set/get y value of the Rectangle
        """
        return self.y
