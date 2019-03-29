"""Unittests for check lucky number."""


import unittest
from task_check_lucky_number.check_lucky_number import is_lucky_number


class TestCheckLucky(unittest.TestCase):
    """Unittests for check lucky number."""

    def test_lucky(self):
        """Test for check lucky number."""
        self.assertTrue(is_lucky_number(123303))

    def test_not_lucky(self):
        """Test for check not lucky number."""
        self.assertFalse(is_lucky_number(123456))

    def test_not_lucky_odd(self):
        """Test for check not lucky number with odd number."""
        with self.assertRaises(Exception):
            is_lucky_number(12345)


if __name__ == '__main__':
    unittest.main()
