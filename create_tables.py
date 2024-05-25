#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from errand_models.errand_models import Base, Errand, User, Product, Cart  # Adjust the import paths if necessary
from os import getenv

# Fetch environment variables
EXPRESS_MYSQL_USER = getenv('EXPRESS_MYSQL_USER')
EXPRESS_MYSQL_PWD = getenv('EXPRESS_MYSQL_PWD')
EXPRESS_MYSQL_HOST = getenv('EXPRESS_MYSQL_HOST')
EXPRESS_MYSQL_DB = getenv('EXPRESS_MYSQL_DB')

# Create an engine
engine = create_engine(f'mysql+mysqldb://{EXPRESS_MYSQL_USER}:{EXPRESS_MYSQL_PWD}@{EXPRESS_MYSQL_HOST}/{EXPRESS_MYSQL_DB}')

# Create the tables
Base.metadata.create_all(engine)

print("Tables created successfully.")

