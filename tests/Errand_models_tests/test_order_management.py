#!/usr/bin/python3

import unittest
from de-errand-xpress import order_management

class TestOrderManagement(unittest.TestCase):
    def setUp(self):
        self.user_id = 'testuser'
        self.order_details = {
            'item': 'Groceries',
            'quantity': 2,
            'address': '123 Main St, Anytown, USA'
        }
        self.order_id = None

        def test_place_order(self):
            response = order_management.place_order(self.user_id, self.order_details)
        self.assertEqual(response.status_code, 201)
        self.assertIn('order_id', response.json())
        self.order_id = response.json()['order_id']

        def test_view_order_status(self):
            response = order_management.place_order(self.user_id, self.order_details)
        self.order_id = response.json()['order_id']

        response = order_management.view_order_status(self.order_id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json())
        self.assertEqual(response.json()['status'], 'Pending')

        def test_update_order(self):
             response = order_management.place_order(self.user_id, self.order_details)
        self.order_id = response.json()['order_id']

        updated_order_details = {
            'item': 'Groceries',
            'quantity': 3,
            'address': '123 Main St, Anytown, USA'
        }
        response = order_management.update_order(self.order_id, updated_order_details)
        self.assertEqual(response.status_code, 200)
        self.assertIn('order_id', response.json())
        self.assertEqual(response.json()['order_id'], self.order_id)

    def test_cancel_order(self):
        response = order_management.place_order(self.user_id, self.order_details)
        self.order_id = response.json()['order_id']

        response = order_management.cancel_order(self.order_id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json())
        self.assertEqual(response.json()['status'], 'Canceled')

if __name__ == '__main__':
    unittest.main()
