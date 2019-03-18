"""Unittests for check function generate Fibonacci sequence."""


import unittest
from task_print_fibonacci_sequence.print_fibonacci_sequence import generate_fibonacci_sequence


class TestGenerateFibonacciSequence(unittest.TestCase):
    """Class for unittests"""

    def test_sequence(self):
        """Unittest for check Fibonacci sequence for max number 34."""
        self.assertEqual(generate_fibonacci_sequence(34), '1 2 3 5 8 13 21 34 ')


if __name__ == '__main__':
    unittest.main()
