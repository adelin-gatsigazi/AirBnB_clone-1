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
            if len(args) < 2:
                print("** instance id missing **")

            class_name = args[0]
            obj_id = args[1]
            key = f"{class_name}.{obj_id}"
            obj_dict = storage.all()

            if key not in obj_dict.keys():
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ Destroy command that destroys an object """
        if arg:
            args = arg.split(" ")

            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
            if len(args) < 2:
                print("** instance id missing **")

            class_name = args[0]
            obj_id = args[1]
            key = f"{class_name}.{obj_id}"
            obj_dict = storage.all()

            if key not in obj_dict.keys():
                print("** no instance found **")
                del obj_dict[key]
                storage.save()
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
        """ Update command that updates an instance """
        args = arg.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        name = args[0]
        obj_id = args[1]
        obj_dict = storage.all()
        key = f"{class_name}.{obj_id}"
        if key not in obj_dict.keys():
            print("** no instance found **")
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) < 4:
            print("** value missing **")
        try:
           if hasattr(obj, args[2]):
               value = type(getattr(key, args[2]))(args[3])
        except (AttributeError, ValueError):
           print("** invalid value **")
        if argv[2] in ("id", "created_at", "updated_at"):
           return
    setattr(key, argv[2], attr_value)
    models.storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
