#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        # TODO: should this be a copy()?
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        # TODO: should these be more precise specifiers?
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj