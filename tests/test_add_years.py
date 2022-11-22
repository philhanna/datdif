from datetime import date
from unittest import TestCase

from date_difference import DateRoller


class TestAddYears(TestCase):

    def test_add_1_year_to_leap_day(self):
        date_roller = DateRoller(date(2020, 2, 29))
        date_roller.add_years(1)
        expected = date(2021, 2, 28)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_add_4_years_to_leap_day(self):
        date_roller = DateRoller(date(2020, 2, 29))
        date_roller.add_years(4)
        expected = date(2024, 2, 29)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_add_4_years_to_non_leap_day(self):
        date_roller = DateRoller(date(2020, 2, 15))
        date_roller.add_years(4)
        expected = date(2024, 2, 15)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_negative_years(self):
        date_roller = DateRoller(date(1953, 12, 4))
        date_roller.add_years(-1)
        expected = date(1952, 12, 4)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_negative_years_on_leap_day(self):
        date_roller = DateRoller(date(2020, 2, 29))
        date_roller.add_years(-3)
        expected = date(2017, 2, 28)
        actual = date_roller.date
        self.assertEqual(expected, actual)

    def test_negative_years_on_leap_day_from_1904(self):
        date_roller = DateRoller(date(1904, 2, 29))
        date_roller.add_years(-4)
        expected = date(1900, 2, 28)
        actual = date_roller.date
        self.assertEqual(expected, actual)


