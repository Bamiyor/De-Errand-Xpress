#!/usr/bin/python3
from os import getenv

storage_type = getenv('EXPRESS_TYPE_STORAGE', 'file')
if storage_type == 'db':
    from errand_models.engine.db_store import DBStorage as Storage
else:
    from errand_models.engine.errand_file_store import FileStorage as Storage

storage = Storage()
storage.reload()
