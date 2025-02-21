# test_integration.py

import unittest
from order_module import calculate_total_price

class TestIntegration(unittest.TestCase):
    def test_order_with_no_discount(self):
        order_items = [
            {'price': 100, 'quantity': 3},
            {'price': 50, 'quantity': 2}
        ]
        self.assertEqual(calculate_total_price(order_items), 400)

    def test_order_with_5_percent_discount(self):
        order_items = [
            {'price': 300, 'quantity': 2},
            {'price': 100, 'quantity': 1}
        ]
        self.assertEqual(calculate_total_price(order_items), 700 * 0.95)

    def test_order_with_10_percent_discount(self):
        order_items = [
            {'price': 500, 'quantity': 3}
        ]
        self.assertEqual(calculate_total_price(order_items), 1500 * 0.9)

if __name__ == '__main__':
    unittest.main()