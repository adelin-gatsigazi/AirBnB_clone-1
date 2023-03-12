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
        obj_dict = storage.all()
        obj_list = []

        if not arg:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            try:
                args = arg.split(" ")
                name = args[0]
                class_name = self.classes[name]
                for obj in obj_dict.values():
                    if type(obj) == class_name:
                        obj_list.append(str(obj))
            except KeyError:
                print("** class doesn't exist **""")
                return
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** instance id missing **")
            return
        objects = storage.all()
        obj_key = args[0] + '.' + args[1]
        if obj_key not in objects:
            print("** no instance found **")
            return
        obj = objects[obj_key]
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(obj, attr_name):
            value = type(getattr(obj, attr_name))(attr_value)
            setattr(obj, attr_name, value)
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()
        print(obj)
        
    def show_obj(self, dic, args):
        """Print out a particular object"""
        dic = storage.all()
        obj = dic[args[0] + "." + args[1]]
        print(obj)

    def destroy(self, dic, args):
        """Destroy an object"""
        del dic[args[0] + "." + args[1]]
        storage.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
