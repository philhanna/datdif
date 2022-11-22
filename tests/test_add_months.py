from datetime import date
from unittest import TestCase

from date_difference import DateRoller


class TestAddMonths(TestCase):

    def test_simple_case(self):
        date_roller = DateRoller(date(1997, 6, 12))
        date_roller.add_months(2)
        expected = date(1997, 8, 12)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_zero_months(self):
        date_roller = DateRoller(date(1997, 6, 12))
        date_roller.add_months(0)
        expected = date(1997, 6, 12)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_through_new_year(self):
        date_roller = DateRoller(date(1953, 12, 4))
        date_roller.add_months(3)
        expected = date(1954, 3, 4)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_back_through_new_year(self):
        date_roller = DateRoller(date(1954, 3, 4))
        date_roller.add_months(-3)
        expected = date(1953, 12, 4)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_leap_day_plus_3(self):
        date_roller = DateRoller(date(2004, 2, 29))
        date_roller.add_months(3)
        expected = date(2004, 5, 31)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_leap_day_backwards_to_previous_year(self):
        date_roller = DateRoller(date(2004, 2, 29))
        date_roller.add_months(-3)
        expected = date(2003, 11, 30)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_non_leap_day_backwards_to_previous_year(self):
        date_roller = DateRoller(date(2005, 2, 28))
        date_roller.add_months(-12)
        expected = date(2004, 2, 29)
        actual = date_roller.date
        self.assertEqual(expected, actual)
