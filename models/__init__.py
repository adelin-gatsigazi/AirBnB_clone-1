#!/usr/bin/python3
""" Initialization of class Filestorage """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
