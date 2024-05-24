#!/usr/bin/python3

import unittest
from de-errand-xpress import place_management

class test_PlaceManagement(unittest.TestCase):
    def setUp(self):
        self.place_details = {
            'name': 'Home',
            'address': '123 Main St',
            'city': 'Anytown',
            'state': 'Anystate',
            'zip_code': '12345'
        }
        self.place_id = None

        def test_create_place(self):
             response = place_management.create_place(
            self.place_details['name'],
            self.place_details['address'],
            self.place_details['city'],
            self.place_details['state'],
            self.place_details['zip_code']
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('place_id', response.json())
        self.place_id = response.json()['place_id']

        def test_get_place(self):
            response = place_management.create_place(
            self.place_details['name'],
            self.place_details['address'],
            self.place_details['city'],
            self.place_details['state'],
            self.place_details['zip_code']
        )
        self.place_id = response.json()['place_id']

        response = place_management.get_place(self.place_id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json())
        self.assertEqual(response.json()['name'], self.place_details['name'])

        def test_update_place
         response = place_management.create_place(
            self.place_details['name'],
            self.place_details['address'],
            self.place_details['city'],
            self.place_details['state'],
            self.place_details['zip_code']
        )
        self.place_id = response.json()['place_id']

        updated_place_details = {
            'name': 'Office',
            'address': '456 Elm St',
            'city': 'Newtown',
            'state': 'Newstate',
            'zip_code': '67890'
        }
        response = place_management.update_place(
            self.place_id,
            updated_place_details['name'],
            updated_place_details['address'],
            updated_place_details['city'],
            updated_place_details['state'],
            updated_place_details['zip_code']
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('place_id', response.json())
        self.assertEqual(response.json()['place_id'], self.place_id)

        def test_delete_place
        response = place_management.create_place(
            self.place_details['name'],
            self.place_details['address'],
            self.place_details['city'],
            self.place_details['state'],
            self.place_details['zip_code']
        )
        self.place_id = response.json()['place_id']

        response = place_management.delete_place(self.place_id)
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        if self.place_id:
            place_management.delete_place(self.place_id)

if __name__ == '__main__':
    unittest.main()
