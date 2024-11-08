from classes.calculator import Calculator
import unittest

class AdditionUnitTests(unittest.TestCase):
 def test_add_positive_numbers_positiv_case(self):

        test_num1 = 5
        test_num2 = 3
        operation = "+"
        expected_result = test_num1 + test_num2

        actual_result = Calculator.calculate(test_num1, test_num2, operation)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()