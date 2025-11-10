import unittest
from testapp import generate_fibonacci


class TestFibonacciGenerator(unittest.TestCase):

    def test_generate_fibonacci_zero(self):
        self.assertEqual(generate_fibonacci(0), [])

    def test_generate_fibonacci_one(self):
        self.assertEqual(generate_fibonacci(1), [0])

    def test_generate_fibonacci_five(self):
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])

    def test_generate_fibonacci_negative(self):
        # The main script handles negative input, but the function itself
        # would produce an empty list for count < 0 if not handled.
        # For now, we'll test the function's direct output.
        self.assertEqual(generate_fibonacci(-1), [])


if __name__ == "__main__":
    unittest.main()
