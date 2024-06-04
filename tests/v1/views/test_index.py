import unittest
from flask import Flask
from flask_testing import TestCase
from api.v1.views.index import app_views
from errand_models import storage
from errand_models.errand_models import User, Product, Errand, Cart
import json

class TestIndex(TestCase):
    def create_app(self):
        """Create a test client for our Flask app"""
        app = Flask(__name__)
        app.register_blueprint(app_views)
        return app

    def setUp(self):
        """Set up test variables"""
        self.client = self.app.test_client
        self.client().testing = True

    def tearDown(self):
        """Tear down test variables"""
        pass

    def test_status(self):
        """Test the /status route"""
        response = self.client().get('/status')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, {"status": "OK"})

    def test_number_objects(self):
        """Test the /stats route"""
        # Mock the storage count method
        def mock_count(cls):
            return {
                User: 5,
                Product: 10,
                Errand: 3,
                Cart: 7
            }[cls]

        storage.count = mock_count

        response = self.client().get('/stats')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        expected_data = {
            "users": 5,
            "products": 10,
            "errands": 3,
            "carts": 7
        }
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
