#!/usr/bin/python3

"""

Command Enterpreter entry point
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """

    Main class of the console
    """
    prompt = "(hbnb) "

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, line):
        """exit"""
        return True

    def do_EOF(self, line):
        """exit"""
        return True

    def emptyline(self):
        "Do nothing"
        pass

    def do_create(self, line):
        """Create a BaseModel object"""
        if not line:
            print("** class name missing **")
        elif line in self.classes.keys():
            obj = self.classes[line]()
            print(obj.id)
            obj.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Print a string representation of an object"""
        if line:
            args = line.split(" ")
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                self.show_obj(storage.all(), args)
            except KeyError:
                """if args[1] os not found"""
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Destroy one object"""
        if line:
            args = line.split(" ")
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                self.destroy(storage.all(), args)

            except KeyError:
                """if args[1] os not found"""
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Print all objects of the same class. Prints all
        objects if no class specified"""
        args = line.split(" ")
        dic = storage.all()
        if line and args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        res = []
        try:
            self.list_objs(dic, self.classes[args[0]], res)
        except KeyError:
            for val in dic.values():
                res.append(str(val))
                print(res)

    def list_objs(self, dic, typ, res):
        """list all objects of a particular type"""
        for val in dic.values():
            if type(val) == typ:
                res.append(str(val))
        print(res)

    def count(self, dic, typ):
        """Count the number of instances of a  class"""
        res = 0
        for val in dic.values():
            if type(val) == typ:
                res += 1
        print(res)

    def show_obj(self, dic, args):
        """Print out a particular object"""
        dic = storage.all()
        obj = dic[args[0] + "." + args[1]]
        print(obj)

    def change_value(self, obj, args):
        """change values of attributes of an object"""
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        try:
            if hasattr(obj, args[2]):
                value = type(getattr(obj, args[2]))(args[3])
                setattr(obj, args[2], value)

        except (TypeError):
            print("** value missing **")

    def destroy(self, dic, args):
        """Destroy an object"""
        del dic[args[0] + "." + args[1]]
        storage.save()

    def do_update(self, line):
        """Update an attribute in an object"""
        if line:
            args = line.split(" ")
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                dic = storage.all()
                obj = dic[args[0] + "." + args[1]]
                self.change_value(obj, args)
                storage.save()
            except KeyError:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def default(self, line):
        """handle some extra methods"""
        rgx = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        args = line.split(".")
        try:
            if args[0] in self.classes.keys() and args[1] == "all()":
                self.list_objs(storage.all(), self.classes[args[0]], [])

            elif args[0] in self.classes.keys() and args[1] == "count()":
                self.count(storage.all(), self.classes[args[0]])

            elif args[0] in self.classes.keys() and "show(" in args[1]:
                args[1] = re.search(rgx, args[1]).group(0)
                self.show_obj(storage.all(), args)

            elif args[0] in self.classes.keys() and "destroy(" in args[1]:
                args[1] = re.search(rgx, args[1]).group(0)
                self.destroy(storage.all(), args)

            else:
                super().default(line)

        except (KeyError, AttributeError):
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
