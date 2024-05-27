#!/usr/bin/python3
from os import getenv

if getenv('EXPRESS_TYPE_STORAGE') == 'db':
    from engine.db_store import DBStorage as Storage
else:
    from errand_models.engine.errand_file_store import FileStorage as Storage

storage = Storage()
storage.reload()

