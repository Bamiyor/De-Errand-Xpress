#!/usr/bin/python3

from sqlalchemy import Column, String, Float, Text
from errand_models.errand_models import BaseModel, Base

class Errand(BaseModel, Base):
    """Representation of an Errand"""
    __tablename__ = 'errands'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float)
    
