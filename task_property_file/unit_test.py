"""Unittests for get property file."""

from os import path

import unittest
from task_property_file.get_property_file import get_property_file


class TestGetPropertyFile(unittest.TestCase):
    """Unittests for get property file."""

    def test_correct_file_utf_8(self):
        """Test for correct file."""
        self.assertEqual(get_property_file(path.join('task_property_file',
                                                        'task_property_file_utf_8.txt')),
                         {'num_line': 21, 'num_word': 76, 'size_file': 753})

    def test_correct_file_cp1251(self):
        """Test for correct file."""
        self.assertEqual(get_property_file(path.join('task_property_file',
                                                        'task_property_file_cp1251.txt')),
                         {'num_line': 21, 'num_word': 76, 'size_file': 444})

    def test_not_exist(self):
        """Test for file doesn't exist."""
        with self.assertRaises(OSError):
            get_property_file('file.txt')


if __name__ == '__main__':
    unittest.main()
