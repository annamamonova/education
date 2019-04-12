"""Unittests for get roots square equation."""

from os import path
import platform

import unittest
from task_square_equation.get_roots_square_equation import get_roots_square_equation


class TestGetRootsSquareEquation(unittest.TestCase):
    """Unittests for get roots square equation."""

    def test_two_roots(self):
        """Test for two roots."""
        self.assertEqual(get_roots_square_equation(1, -2, -3), [3.0, -1.0])

    def test_one_root(self):
        """Test for one root."""
        self.assertEqual(get_roots_square_equation(1, 12, 36), [-6.0])

    def test_not_roots(self):
        """Test for not roots."""
        self.assertEqual(get_roots_square_equation(5, 3, 7), "Not roots.")


if __name__ == '__main__':
    unittest.main()
