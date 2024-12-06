import unittest
from simple_calcs import SimpleCalcs

class TestCalcs(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalcs()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(4, 4), 16) 

    def test_division(self):
        self.assertEqual(self.calc.division(6, 3), 2)

    def test_zero_division(self):
        self.assertEqual(self.calc.division(1, 0), "Cannot divide by zero!")           

if __name__ == '__main__':
    unittest.main()