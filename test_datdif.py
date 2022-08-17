from unittest import TestCase
from datetime import date, datetime, timedelta

from datdif import datdif, DEFAULT_START_DATE, DEFAULT_END_DATE


class TestDatdif(TestCase):

    def test_both_dates(self):
        start_date = date(2022, 8, 16)
        end_date = date(2022, 8, 23)
        expected = 7
        actual = datdif(start_date, end_date)
        self.assertEqual(expected, actual)

    def test_only_one_date(self):
        end_date: date = date(2040, 1, 1)
        expected = (end_date - DEFAULT_START_DATE).days
        actual: int = datdif(end_date)
        self.assertEqual(expected, actual)

    def test_no_dates(self):
        start_date = DEFAULT_START_DATE
        end_date = DEFAULT_END_DATE
        print(datdif())
