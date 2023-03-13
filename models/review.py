#!usr/bin/python3
"""Module for a Review state """

from models.base_model import BaseModel


class Review(BaseModel):
    """class representing a Review"""
    place_id = ""
    user_id = ""
    text = ""
