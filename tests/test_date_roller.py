from datetime import date
from unittest import TestCase

from datdif import DateRoller


class TestDateRoller(TestCase):

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