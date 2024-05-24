    #!/usr/bin/python3
from errand_models.errand_models import Errand, Base
from sqlalchemy import Column, String, Float

"""
import  errand_models
from  errand_models.errand_models  import errand_models
from sqlalchemy import Column, String
from errand_models.engine import db_store, db

class Product(db.errand_models):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))
    # Add more product attributes as needed
    """

class Product(Base):
    """Representation of a product"""
    __tablename__ = 'products'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String(256))
