#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from errand_models.db_storage import DBStore
from errand_models.errand_models import Base, Cart, Product, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.patcher1 = patch('errand_models.db_storage.getenv', side_effect=lambda key: {
            'EXPRESS_MYSQL_USER': 'test_user',
            'EXPRESS_MYSQL_PWD': 'test_pwd',
            'EXPRESS_MYSQL_HOST': 'localhost',
            'EXPRESS_MYSQL_DB': 'test_db',
            'EXPRESS_ENV': 'test'
        }.get(key))
        self.mock_getenv = self.patcher1.start()

        self.storage = DBStorage()
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.Session)
        self.storage._DBStorage__session = self.session

    def tearDown(self):
        """Tear down the test environment"""
        self.session.remove()
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()
        self.patcher1.stop()

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test that new() adds an object to the session"""
        user = User(name="John Doe", email="john@example.com", password="password123")
        self.storage.new(user)
        self.assertIn(user, self.session.new)

    def test_all_with_class(self):
        """Test that all(cls) returns a dictionary of objects of that class"""
        user1 = User(name="John Doe", email="john1@example.com", password="password123")
        user2 = User(name="Jane Doe", email="jane@example.com", password="password123")
        self.session.add(user1)
        self.session.add(user2)
        self.session.commit()

        result = self.storage.all(User)
        self.assertIsInstance(result, dict)
        self.assertIn('User.' + user1.id, result)
        self.assertIn('User.' + user2.id, result)

if __name__ == '__main__':
    unittest.main()
