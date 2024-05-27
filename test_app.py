#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from flask_testing import TestCase
from app import app

class TestAppRoutes(TestCase):
    def create_app(self):
        """Create a Flask app for testing"""
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """Set up the test environment"""
        self.client = self.app.test_client()
        self.client.testing = True

    @patch('app.storage')
    def test_index_route(self, mock_storage):
        """Test index route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Errand Express', response.data)

    @patch('app.storage')
    def test_products_route(self, mock_storage):
        """Test products route"""
        mock_storage.all.return_value = [MagicMock(name="Product1"), MagicMock(name="Product2")]
        response = self.client.get('/product')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product1', response.data)
        self.assertIn(b'Product2', response.data)

    @patch('app.storage')
    def test_cart_route_GET(self, mock_storage):
        """Test cart route (GET request)"""
        mock_storage.all.return_value = [MagicMock(name="Cart1"), MagicMock(name="Cart2")]
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cart1', response.data)
        self.assertIn(b'Cart2', response.data)

    @patch('app.storage')
    def test_cart_route_POST(self, mock_storage):
        """Test cart route (POST request)"""
        mock_request = MagicMock(form={'product_id': '1', 'quantity': '2', 'user_id': '1'})
        with patch('app.request', mock_request):
            response = self.client.post('/cart')
        self.assertEqual(response.status_code, 302)  # Redirects after POST

if __name__ == '__main__':
    unittest.main()
