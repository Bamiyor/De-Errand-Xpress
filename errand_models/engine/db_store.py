#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from errand_models import Base, Cart, Product, User # Corrected import path

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        EXPRESS_MYSQL_USER = getenv('EXPRESS_MYSQL_USER')
        EXPRESS_MYSQL_PWD = getenv('EXPRESS_MYSQL_PWD')
        EXPRESS_MYSQL_HOST = getenv('EXPRESS_MYSQL_HOST')
        EXPRESS_MYSQL_DB = getenv('EXPRESS_MYSQL_DB')
        EXPRESS_ENV = getenv('EXPRESS_ENV')
        self.__engine = create_engine(f'mysql+mysqldb://{EXPRESS_MYSQL_USER}:{EXPRESS_MYSQL_PWD}@{EXPRESS_MYSQL_HOST}/{EXPRESS_MYSQL_DB}')
        if EXPRESS_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from errand_models.errand_models import Cart, Product, User  # Local import to avoid circular import
        classes = {"Cart": Cart, "Product": Product, "User": User}
        
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class name and its ID, or None if not found"""
        from errand_models import storage  # Local import to avoid circular import
        all_cls = storage.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value
        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        from errand_models import storage  # Local import to avoid circular import
        all_class = [Cart, Product, User]
        if not cls:
            count = 0
            for clas in all_class:
                count += len(storage.all(clas).values())
        else:
            count = len(storage.all(cls).values())
        return count
