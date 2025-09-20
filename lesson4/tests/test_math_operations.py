import unittest
import utils.math_operations

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(utils.math_operations.add(2, 3), 5)
        self.assertEqual(utils.math_operations.add(-1, 1), 0)
        self.assertEqual(utils.math_operations.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(utils.math_operations.subtract(5, 3), 2)
        self.assertEqual(utils.math_operations.subtract(0, 1), -1)


if __name__ == '__main__':
    unittest.main()
