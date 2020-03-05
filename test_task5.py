from unittest import TestCase

import task5


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_sd_in_range(self):
        self.assertEqual(task5.sd_in_range(['1', '4']), [1, 2, 3, 4])
        self.assertEqual(task5.sd_in_range(['1', '22']),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
        self.assertEqual(task5.sd_in_range(['0', '11']),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 11])

    def tearDown(self):
        """Finish"""
