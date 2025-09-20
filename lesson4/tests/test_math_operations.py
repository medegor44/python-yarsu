import unittest
import utils.math_operations

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # Arrange
        a = 2
        b = 3
        expected = 5
        # Act
        actual = utils.math_operations.add(a, b)
        # Assert
        self.assertEqual(actual, expected)

    def test_multiply_regular_usage_should_respond_correctly(self):
        # Arrange
        a = 2
        b = 3
        expected = 6
        # Act
        actual = utils.math_operations.multiply(a, b)
        # Assert
        self.assertEqual(actual, expected)

    def test_subtract(self):
        # Arrange
        a = 5
        b = 3
        expected = 2
        # Act
        actual = utils.math_operations.subtract(a, b)
        # Assert
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
