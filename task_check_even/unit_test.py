import unittest
from task_check_even.check_even import is_even


class TestCheckEven(unittest.TestCase):

    def test_even(self):
        self.assertTrue(is_even(4))

    def test_odd(self):
        self.assertFalse(is_even(3))


if __name__ == '__main__':
    unittest.main()
