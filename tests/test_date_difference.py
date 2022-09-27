from datetime import date
from unittest import TestCase
from unittest.mock import patch

from datdif import DateDifferencer


class TestDateDifference(TestCase):

    def test_two_days(self):
        start_date = date(2020, 1, 1)
        end_date = date(2020, 1, 3)
        dd = DateDifferencer(start_date, end_date)
        expected = 2
        actual = dd.delta()
        self.assertEqual(expected, actual)

    def test_one_year(self):
        start_date = "3/2/1975"
        end_date = "3/2/1976"
        dd = DateDifferencer(start_date, end_date)
        expected = 366
        actual = dd.delta()
        self.assertEqual(expected, actual)

    def test_today_tomorrow(self):
        with patch('datdif.DateDifferencer.current_date') as mock_current_date:
            mock_current_date.return_value = date(2020, 1, 1)
            start_date = "today"
            end_date = date(2020, 1, 2)
            expected = 1
            dd = DateDifferencer(start_date, end_date)
            actual = dd.delta()
            self.assertEqual(expected, actual)
