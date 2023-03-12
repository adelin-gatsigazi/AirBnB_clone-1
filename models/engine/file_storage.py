#!/usr/bin/python3
""" Stores objects in Json Format """
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel}

    def all(self):
        """ returns the object dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets a new key-value pair object and stores it in
        the dictionnary """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes objects """
        file_obj = {}

        for key, value in FileStorage.__objects.items():
            file_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(file_obj, f)

    def reload(self):
        """ Deserializes the object """
        data = {}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)

        for key, value in data.items():
            obj_class_name, obj_id = key.split('.')
            class_name = FileStorage.classes[obj_class_name]
            obj = class_name(**value)
            FileStorage.__objects[key] = obj
        else:
            return
