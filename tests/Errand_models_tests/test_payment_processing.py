#!/usr/bin/python3

import unittest
from de-errand-xpress import payment_processing

class TestPaymentProcessing(unittest.TestCase):

    def test_successful_payment(self):
        response = payment_processing.process_payment('order_id', 'valid_payment_details')
        self.assertEqual(response.status_code, 200)
        self.assertIn('payment_id', response.json()

        def test_failed_payment_insufficient_funds(self):
            response = payment_processing.process_payment('order_id', 'insufficient_funds_details')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

            def test_failed_payment_invalid_card(self):
                response = payment_processing.process_payment('order_id', 'invalid_card_details')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())


if __name__ == '__main__':
    unittest.main()
