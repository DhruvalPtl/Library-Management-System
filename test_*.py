# test_calculator_unittest.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(2, 0), 2)
        self.assertEqual(subtract(2, -2), 4)

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            add("one", "two")

if __name__ == '__main__':
    unittest.main()