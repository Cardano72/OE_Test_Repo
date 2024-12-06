import unittest
from simple_calcs import SimpleCalcs

class TestIntegration(unittest.TestCase):
    def test_combined_operations(self):
        calc = SimpleCalcs()
        result = calc.addition(3, 3) - calc.division(8, 4)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()