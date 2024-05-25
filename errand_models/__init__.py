#!/usr/bin/python3
from os import getenv

if getenv('EXPRESS_TYPE_STORAGE') == 'db':
    from engine.db_store import DBStorage as Storage
else:
    from engine.errand_file_store import FileStorage as Storage

storage = Storage()
storage.reload()
"""
from os import getenv
from errand_models.engine.db_store import DBStorage
from errand_models.engine.errand_file_store import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
"""
