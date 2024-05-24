#!/usr/bin/python3
from errand_models.errand_models import Errand, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Cart(Base):
    """Representation of a cart"""
    __tablename__ = 'carts'
    id = Column(String(60), primary_key=True, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

"""
import  errand_models
from  errand_models.errand_models  import errand_models
from sqlalchemy import Column, String
from errand_models.engine import db_store, db

class Cart(db.errand_models):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    """