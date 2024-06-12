#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from errand_models.errand_models import Base, Cart, Product, User

class DBStorage:
    __engine = None
    __session = None


    def __init__(self):
        EXPRESS_MYSQL_USER = 'xpress_user'
        EXPRESS_MYSQL_PWD = 'xpress_password'
        EXPRESS_MYSQL_HOST = 'localhost'
        EXPRESS_MYSQL_DB = 'xpress_db'
        EXPRESS_ENV = 'dev'
        self.__engine = create_engine(f'mysql+mysqldb://{EXPRESS_MYSQL_USER}:{EXPRESS_MYSQL_PWD}@{EXPRESS_MYSQL_HOST}/{EXPRESS_MYSQL_DB}')
        if EXPRESS_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from errand_models.errand_models import Cart, Product, User
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
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        self.__session.remove()

    def get(self, cls, id):
        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value
        return None

    def count(self, cls=None):
        all_class = [Cart, Product, User]
        if not cls:
            count = 0
            for clas in all_class:
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())
        return count
