#!/usr/bin/python3
"""
Inherits from the Base class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Deifining a square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing class
        """
        super().__init__(size, size, x, y, id)
        self.size = self.width

    @property
    def size(self):
        """
        Get property
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size> - to stdout
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
