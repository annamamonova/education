"""Unittests for check function generate ab sequence."""


import unittest
from print_ab_sequence import generate_ab_sequence


class TestGenerateAbSequence(unittest.TestCase):
    """Class for unittests"""

    def test_sequence(self):
        """Unittest for check ab sequence for number 1 to 12."""
        self.assertEqual(generate_ab_sequence(1, 12), '1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ')


if __name__ == '__main__':
    unittest.main()
