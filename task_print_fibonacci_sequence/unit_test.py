"""Unittests for check function generate Fibonacci sequence."""


import unittest
from print_fibonacci_sequence import generate_fibonacci_sequence


class TestGenerateFibonacciSequence(unittest.TestCase):
    """Class for unittests"""

    def test_sequence(self):
        """Unittest for check Fibonacci sequence for max counter 21."""
        self.assertEqual(generate_fibonacci_sequence(21),
                         [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                          987, 1597, 2584, 4181, 6765, 10946, 17711])

    def test_sequence_min(self):
        """Unittest for check Fibonacci sequence for max counter 1."""
        self.assertEqual(generate_fibonacci_sequence(1), [1])


if __name__ == '__main__':
    unittest.main()
