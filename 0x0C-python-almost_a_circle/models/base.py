#!/usr/bin/python3
"""
a module for base class
"""


class Base:
    """
    Defining a base class module
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        a constructor function
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
