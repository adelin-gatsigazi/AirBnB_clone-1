#!/usr/bin/python3
"""Module for City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """class representing a City."""
    state_id: str = ""
    name: str = ""
