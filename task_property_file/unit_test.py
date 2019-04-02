"""Unittests for get property file."""


import os
import unittest
from task_property_file.get_property_file import get_property_file


class TestGetPropertyFile(unittest.TestCase):
    """Unittests for get property file."""

    def test_correct_file(self):
        """Test for correct file."""
        print(os.getcwd())
        self.assertEqual(get_property_file('task_property_file.txt'),
                         {'num_line': 21, 'num_word': 76, 'size_file': 444})

    def test_not_exist(self):
        """Test for file doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            get_property_file('file.txt')


if __name__ == '__main__':
    unittest.main()
