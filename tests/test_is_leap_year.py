from unittest import TestCase

from datdif import is_leap_year


class TestIsLeapYear(TestCase):
    """Unit tests for is_leap_year"""

    def test_2001_is_leap_year(self):
        self.assertFalse(is_leap_year(2001))

    def test_2018_is_leap_year(self):
        self.assertFalse(is_leap_year(2018))

    def test_2000_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))

    def test_1900_is_leap_year(self):
        self.assertFalse(is_leap_year(1900))

    def test_2020_is_leap_year(self):
        self.assertTrue(is_leap_year(2020))
