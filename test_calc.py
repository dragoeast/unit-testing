import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-2, -3), -5)

    def test_substruct(self):
        self.assertEqual(calc.substruct(10, 5), 5)
        self.assertEqual(calc.substruct(1, -1), 2)
        self.assertEqual(calc.substruct(-2, -3), 1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, -1), -1)
        self.assertEqual(calc.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-6, -3), 2)

        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == "__main__":
    unittest.main()
