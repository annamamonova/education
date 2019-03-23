"""Unittests for check even."""


import unittest
from check_even import is_even


class TestCheckEven(unittest.TestCase):
    """Unittests for check even."""

    def test_even(self):
        """Test for check even."""
        self.assertTrue(is_even(4))

    def test_odd(self):
        """Test for check odd."""
        self.assertFalse(is_even(3))


if __name__ == '__main__':
    unittest.main()
