# test_discount_module.py

import unittest
from discount_module import apply_discount

class TestDiscountModule(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(apply_discount(400), 400)
        self.assertEqual(apply_discount(500), 500)

    def test_5_percent_discount(self):
        self.assertEqual(apply_discount(600), 600 * 0.95)
        self.assertEqual(apply_discount(1000), 1000 * 0.95)

    def test_10_percent_discount(self):
        self.assertEqual(apply_discount(1100), 1100 * 0.9)
        self.assertEqual(apply_discount(2000), 2000 * 0.9)

if __name__ == '__main__':
    unittest.main()