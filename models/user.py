#!/usr/bin/python3
""" class User that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines the attributes of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
