#!/usr/bin/python3
""" console for the project """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Handles the command"""

    prompt = "(hbnb)"

    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print("")
        return True

    def emptyline(self):
        """ Emptyline command that executes nothing """
        pass

    def do_create(self, arg):
        """ Create command to create a new object """
        if not arg:
            print("** class name missing **")
        elif arg in self.classes.keys():
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Show Command that prints the string representation
        of an object """
        if arg:
            args = arg.split(" ")

            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")

            try:
                self.show_obj(storage.all(), args)
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ Destroy command that destroys an object """
        if arg:
            args = arg.split(" ")

            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
            try:
                self.destroy(storage.all(), args)

            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """" All command that prints all instances
        in string representation """
        args = arg.split(" ")
        dic = storage.all()
        if arg and args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        obj_list = []
        try:
            self.list_obj(dic, self.classes[args[0]], obj_list)
        except KeyError:
            for val in dic.values():
                obj_list.append(str(val))
            print(obj_list)

    def do_update(self, arg):
        """ Update command that updates an instance """
        if arg:
            args = arg.split(" ")
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

    def list_obj(self, dic, class_name, obj_list):
        """ Creates and prints a list """
        for val in dic.values:
            if type(val) == class_name:
                obj_list.append(str(val))

        print(obj_list)

    def show_obj(self, dic, args):
        """Print out a particular object"""
        dic = storage.all()
        obj = dic[args[0] + "." + args[1]]
        print(obj)

    def destroy(self, dic, args):
        """Destroy an object"""
        del dic[args[0] + "." + args[1]]
        storage.save()

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
            else:
                setattr(obj, args[2], args[3])
        except TypeError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
