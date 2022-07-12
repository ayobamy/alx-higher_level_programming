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

    @staticmethod
    def from_json_string(json_string):
        """
        load list of objects from json string
        :param json_string: json string
        :return: JSON string representation of list of objects
        """
        if (json_string is None or json_string == "[]"):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create new list of objects
        :param dictionary: dict object
        :return: list of objects
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_values = cls(1, 1)
            else:
                new_values = cls(1)
            new_values.update(**dictionary)
            return new_values

    @classmethod
    def load_from_file(cls):
        """
        load list of objects from file
        :return: list of objects
        """
        filename = "{}.json".format(cls.__name__)

        if not filename:
            return []
        else:
            with open(filename, "r", encoding="utf-8") as f:
                return [cls.create(**instances) for instances
                        in cls.from_json_string(f.read())]
