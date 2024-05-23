#!/usr/bin/python3
"""
import  errand_models
from  errand_models.errand_models  import errand_models
from sqlalchemy import Column, String
from errand_models.engine import db_store, db

class User(db.errand_models):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
"""
from errand_models.errand_models import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5

class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    carts = relationship("Cart", backref="user")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

