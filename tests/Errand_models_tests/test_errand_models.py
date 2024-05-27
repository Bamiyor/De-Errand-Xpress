#!/usr/bin/python3

import unittest
from datetime import datetime
from errand_models.errand_models import BaseModel, Errand, User, Product, Cart
import uuid
from hashlib import md5

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()
    
    def test_id(self):
        self.assertIsInstance(self.base.id, str)
        self.assertEqual(len(self.base.id), 36)  # UUID4 has 36 characters including hyphens

    def test_created_at(self):
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_save(self):
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at, old_updated_at)

    def test_to_dict(self):
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['id'], self.base.id)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['created_at'], self.base.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_dict['updated_at'], self.base.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

class TestErrand(unittest.TestCase):
    def setUp(self):
        self.errand = Errand(name="Grocery Shopping", description="Buy groceries", price=100.0)
    
    def test_errand_attributes(self):
        self.assertEqual(self.errand.name, "Grocery Shopping")
        self.assertEqual(self.errand.description, "Buy groceries")
        self.assertEqual(self.errand.price, 100.0)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(name="John Doe", email="john@example.com", password="password123")

    def test_user_attributes(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.password, md5("password123".encode()).hexdigest())

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(name="Laptop", price=999.99, image_url="http://example.com/laptop.jpg")

    def test_product_attributes(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.image_url, "http://example.com/laptop.jpg")

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart(user_id=str(uuid.uuid4()), product_id=str(uuid.uuid4()), quantity=2)
    
    def test_cart_attributes(self):
        self.assertIsInstance(self.cart.user_id, str)
        self.assertIsInstance(self.cart.product_id, str)
        self.assertEqual(self.cart.quantity, 2)

if __name__ == '__main__':
    unittest.main()
