#!/usr/bin/python3
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy.orm import relationship, Integer, ForeignKey
from hashlib import md5
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("EXPRESS_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if getenv("EXPRESS_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)

class Errand(BaseModel, Base):
    """Representation of an Errand"""
    __tablename__ = 'errands'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float)

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

class Product(BaseModel, Base):
    """Representation of a product"""
    __tablename__ = 'products'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String(256))

class Cart(BaseModel, Base):
    """Representation of a cart"""
    __tablename__ = 'carts'
    id = Column(String(60), primary_key=True, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
