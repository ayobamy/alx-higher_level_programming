#!/usr/bin/python3
"""
a module for base class
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list of dictionaries to json string
        :param list_dictionaries: list of dictionaries
        :return: json string
        """
        if (list_dictionaries is None or list_dictionaries == []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save list of objects to file
        :param list_objs: list of objects
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            if (list_objs is None or len(list_objs) == 0):
                file.write("[]")
            else:
                list_dict = [list.to_dictionary() for list in list_objs]
                file.write(cls.to_json_string(list_dict))
