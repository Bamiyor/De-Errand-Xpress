#!/usr/bin/python3
from errand_models.engine import db_store
from errand_models.user import User
from errand_models.cart import Cart
from errand_models.product import Product

from os import getenv
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage as Storage
else:
    from models.engine.file_storage import FileStorage as Storage

storage = Storage()
storage.reload()
