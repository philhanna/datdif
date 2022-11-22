from unittest import TestCase

from date_difference import get_max_days


class TestMaxDays(TestCase):
    """Unit tests for get_max_days"""

    def test_get_max_days_2018_2(self):
        self.assertEqual(28, get_max_days(2018, 2))

    def test_get_max_days_2020_2(self):
        self.assertEqual(29, get_max_days(2020, 2))

    def test_get_max_days_2000_2(self):
        self.assertEqual(29, get_max_days(2000, 2))

    def test_get_max_days_2000_4(self):
        self.assertEqual(30, get_max_days(2000, 4))

    def test_get_max_days_1953_12(self):
        self.assertEqual(31, get_max_days(1953, 12))

