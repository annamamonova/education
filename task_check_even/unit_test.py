# unittests for check even
import unittest
from task_check_even.check_even import is_even


# unittests for check even
class TestCheckEven(unittest.TestCase):

    # test for check even
    def test_even(self):
        self.assertTrue(is_even(4))

    # test for check odd
    def test_odd(self):
        self.assertFalse(is_even(3))


if __name__ == '__main__':
    unittest.main()
