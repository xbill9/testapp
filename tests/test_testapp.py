import unittest
from testapp import generate_lucas


class TestLucasGenerator(unittest.TestCase):

    def test_generate_lucas_zero(self):
        self.assertEqual(generate_lucas(0), [])

    def test_generate_lucas_one(self):
        self.assertEqual(generate_lucas(1), [2])

    def test_generate_lucas_five(self):
        self.assertEqual(generate_lucas(5), [2, 1, 3, 4, 7])

    def test_generate_lucas_negative(self):
        # The main script handles negative input, but the function itself
        # would produce an empty list for count < 0 if not handled.
        # For now, we'll test the function's direct output.
        self.assertEqual(generate_lucas(-1), [])


if __name__ == "__main__":
    unittest.main()
