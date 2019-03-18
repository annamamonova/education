import unittest
from task_print_ab_sequence.print_ab_sequence import print_ab_sequence


class TestPrintAbSequence(unittest.TestCase):

    def test_sequence(self):
        self.assertEqual(print_ab_sequence(1, 12), '1 2a 3b 4a 5 6ab 7 8a 9b 10a 11 12ab ')


if __name__ == '__main__':
    unittest.main()
