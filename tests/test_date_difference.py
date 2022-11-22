from datetime import date, timedelta
from unittest import TestCase
from unittest.mock import patch

from date_difference import DateDifferencer


class TestDateDifference(TestCase):

    def test_two_days(self):
        start_date = date(2020, 1, 1)
        end_date = date(2020, 1, 3)
        dd = DateDifferencer(start_date, end_date, days=False)
        expected = (0, 0, 2)
        actual = dd.delta
        self.assertTupleEqual(expected, actual)

    def test_two_days_in_days(self):
        start_date = date(2020, 1, 1)
        end_date = date(2020, 1, 3)
        dd = DateDifferencer(start_date, end_date, days=True)
        expected = 2
        actual = dd.delta
        self.assertEqual(expected, actual)

    def test_two_days_with_date_string_in_days(self):
        start_date = "2020-01-01"
        end_date = date(2020, 1, 3)
        dd = DateDifferencer(start_date, end_date, days=True)
        expected = 2
        actual = dd.delta
        self.assertEqual(expected, actual)

    def test_one_year(self):
        start_date = "1975-03-02"
        end_date = "1976-03-02"
        dd = DateDifferencer(start_date, end_date, days=False)
        expected = (1, 0, 0)
        actual = dd.delta
        self.assertTupleEqual(expected, actual)
        self.assertEqual("1 year", str(dd))

    def test_one_year_in_days(self):
        start_date = "1975-03-02"
        end_date = "1976-03-02"
        dd = DateDifferencer(start_date, end_date, days=True)
        expected = 366
        actual = dd.delta
        self.assertEqual(expected, actual)

    def test_today_tomorrow_in_days(self):
        with patch('date_difference.DateDifferencer.current_date') as mock_current_date:
            mock_current_date.return_value = date(2020, 1, 1)
            start_date = "today"
            end_date = "2020-01-02"
            expected = 1
            dd = DateDifferencer(start_date, end_date, days=True)
            actual = dd.delta
            self.assertEqual(expected, actual)

    def test_then_to_now(self):
        start_date = "1953-12-04"
        end_date = "2022-09-26"
        dd = DateDifferencer(start_date, end_date, days=False)
        expected = (68, 9, 22)
        actual = dd.delta
        self.assertTupleEqual(expected, actual)

    def test_then_to_jfk(self):
        start_date = "1953-12-04"
        end_date = "1963-11-22"
        dd = DateDifferencer(start_date, end_date, days=False)
        self.assertTupleEqual((9, 11, 18), dd.delta)

    def test_str_one_day(self):
        start_date = "1953-12-31"
        end_date = "1954-01-01"
        dd = DateDifferencer(start_date, end_date, days=False)
        expected = "1 day"
        actual = str(dd)
        self.assertEqual(expected, actual)

    def test_str_two_days_from_leap_day(self):
        start_date = "2000-02-28"
        end_date = "2000-03-01"
        dd = DateDifferencer(start_date, end_date, days=False)
        self.assertTupleEqual((0, 0, 2), dd.delta)
        expected = "2 days"
        actual = str(dd)
        self.assertEqual(expected, actual)

    def test_today(self):
        start_date = "today"
        td = timedelta(days=1)
        end_date = date.today() + td
        dd = DateDifferencer(start_date, end_date, days=False)
        self.assertTupleEqual((0, 0, 1), dd.delta)
        expected = "1 day"
        actual = str(dd)
        self.assertEqual(expected, actual)

    def test_zero(self):
        start_date = "1922-01-04"
        end_date = start_date
        dd = DateDifferencer(start_date, end_date, days=False)
        self.assertTupleEqual((0, 0, 0), dd.delta)

    def test_zero_in_days(self):
        start_date = "1922-01-04"
        end_date = start_date
        dd = DateDifferencer(start_date, end_date, days=True)
        self.assertEqual(0, dd.delta)

    def test_bad(self):
        start_date = "1922-01-04"
        end_date = "1901-01-04"
        with self.assertRaises(ValueError) as ex:
            DateDifferencer(start_date, end_date, days=False)
        expected = "cannot be"
        self.assertIn(expected, str(ex.exception))

    def test_bad_in_days(self):
        start_date = "1922-01-04"
        end_date = "1901-01-04"
        with self.assertRaises(ValueError) as ex:
            DateDifferencer(start_date, end_date, days=True)
        expected = "cannot be"
        self.assertIn(expected, str(ex.exception))

    def test_failing_days(self):
        start_date = "2019-02-23"
        end_date = "today"
        dd = DateDifferencer(start_date, end_date, days=True)
        #print(dd)
