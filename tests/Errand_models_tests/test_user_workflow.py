#!/usr/bin/python3

import unittest
from de-errand-xpress import user_management

Class TestUserWorkflow(unittest.TestCase):
    def test_user_registration(self):
        response = user_management.register_user('testuser', 'Test@1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json())

        response = user_management.register_user('', 'weakpassword')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())


        def test_user_login(self):
            response = user_management.login_user('testuser', 'Test@1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json())

        response = user_management.login_user('testuser', 'wrongpassword')
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.json())

        def test_user_logout(self):
            access_token = response.json().get('access_token')
        logout_response = user_management.logout_user(access_token)
        self.assertEqual(logout_response.status_code, 200)
        self.assertIn('message', logout_response.json())
        self.assertEqual(logout_response.json()['message'], 'Logged out successfully')

if __name__ == '__main__':
    unittest.main()
