#!/usr/bin/python3

import unittest
from de_errand_xpress import review_management

class TestReviewManagement(unittest.TestCase):
    def setUp(self):
        self.user_id = 'testuser'
        self.service_id = 'testservice'
        self.review_details = {
            'rating': 5,
            'comment': 'Excellent service!',
            'reviewer_id': self.user_id,
            'service_id': self.service_id
        }
        self.review_id = None

    def test_create_review(self):
        response = review_management.create_review(
            self.review_details['rating'],
            self.review_details['comment'],
            self.review_details['reviewer_id'],
            self.review_details['service_id']
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('review_id', response.json())
        self.review_id = response.json()['review_id']

    def test_get_review(self):
        response = review_management.create_review(
            self.review_details['rating'],
            self.review_details['comment'],
            self.review_details['reviewer_id'],
            self.review_details['service_id']
        )
        self.review_id = response.json()['review_id']

        response = review_management.get_review(self.review_id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('rating', response.json())
        self.assertEqual(response.json()['rating'], self.review_details['rating'])

    def test_update_review(self):
        response = review_management.create_review(
            self.review_details['rating'],
            self.review_details['comment'],
            self.review_details['reviewer_id'],
            self.review_details['service_id']
        )
        self.review_id = response.json()['review_id']

        updated_review_details = {
            'rating': 4,
            'comment': 'Good service.',
        }
        response = review_management.update_review(
            self.review_id,
            updated_review_details['rating'],
            updated_review_details['comment']
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('review_id', response.json())
        self.assertEqual(response.json()['review_id'], self.review_id)

    def test_delete_review(self):
        response = review_management.create_review(
            self.review_details['rating'],
            self.review_details['comment'],
            self.review_details['reviewer_id'],
            self.review_details['service_id']
        )
        self.review_id = response.json()['review_id']

        response = review_management.delete_review(self.review_id)
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        if self.review_id:
            review_management.delete_review(self.review_id)

if __name__ == '__main__':
    unittest.main()

