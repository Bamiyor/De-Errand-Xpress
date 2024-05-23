#!/usr/bin/python3

import unittest
from de-errand-xpress import user_management

class TestUserManagement(unittest.TestCase):
    def test_user_registration_valid_data(self):
        response = user_management.register_user('testuser', 'Test@1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())

    if __name__ == '__main__':
        unittest.main()

