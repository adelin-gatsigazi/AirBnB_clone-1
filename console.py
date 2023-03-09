#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    
    def do_quit(self, arg):
        """command  exit the program."""
        return True
    
    def emptyline(self):
        """Do not do anything for recieving an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

if __name__ == '__main__':
    TurtleShell().cmdloop()

