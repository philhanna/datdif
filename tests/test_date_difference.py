from datetime import date, timedelta

import pytest

from date_difference import DateDifferencer


def test_two_days():
    start_date = date(2020, 1, 1)
    end_date = date(2020, 1, 3)
    dd = DateDifferencer(start_date, end_date, days=False)
    expected = (0, 0, 2)
    actual = dd.delta
    assert actual == expected


def test_two_days_in_days():
    start_date = date(2020, 1, 1)
    end_date = date(2020, 1, 3)
    dd = DateDifferencer(start_date, end_date, days=True)
    expected = 2
    actual = dd.delta
    assert actual == expected


def test_two_days_with_date_string_in_days():
    start_date = "2020-01-01"
    end_date = date(2020, 1, 3)
    dd = DateDifferencer(start_date, end_date, days=True)
    expected = 2
    actual = dd.delta
    assert actual == expected


def test_one_year():
    start_date = "1975-03-02"
    end_date = "1976-03-02"
    dd = DateDifferencer(start_date, end_date, days=False)
    expected = (1, 0, 0)
    actual = dd.delta
    assert actual == expected
    assert str(dd) == "1 year"


def test_one_year_in_days():
    start_date = "1975-03-02"
    end_date = "1976-03-02"
    dd = DateDifferencer(start_date, end_date, days=True)
    expected = 366
    actual = dd.delta
    assert actual == expected


def test_today_tomorrow_in_days(monkeypatch):
    monkeypatch.setattr('date_difference.DateDifferencer.current_date', lambda: date(2020, 1, 1))
    start_date = "today"
    end_date = "2020-01-02"
    expected = 1
    dd = DateDifferencer(start_date, end_date, days=True)
    actual = dd.delta
    assert actual == expected


def test_then_to_now():
    start_date = "1953-12-04"
    end_date = "2022-09-26"
    dd = DateDifferencer(start_date, end_date, days=False)
    expected = (68, 9, 22)
    actual = dd.delta
    assert actual == expected


def test_then_to_jfk():
    start_date = "1953-12-04"
    end_date = "1963-11-22"
    dd = DateDifferencer(start_date, end_date, days=False)
    assert dd.delta == (9, 11, 18)


def test_str_one_day():
    start_date = "1953-12-31"
    end_date = "1954-01-01"
    dd = DateDifferencer(start_date, end_date, days=False)
    expected = "1 day"
    actual = str(dd)
    assert actual == expected


def test_str_two_days_from_leap_day():
    start_date = "2000-02-28"
    end_date = "2000-03-01"
    dd = DateDifferencer(start_date, end_date, days=False)
    assert dd.delta == (0, 0, 2)
    expected = "2 days"
    actual = str(dd)
    assert actual == expected


def test_today():
    start_date = "today"
    td = timedelta(days=1)
    end_date = date.today() + td
    dd = DateDifferencer(start_date, end_date, days=False)
    assert dd.delta == (0, 0, 1)
    expected = "1 day"
    actual = str(dd)
    assert actual == expected


def test_zero():
    start_date = "1922-01-04"
    end_date = start_date
    dd = DateDifferencer(start_date, end_date, days=False)
    expected = (0, 0, 0)
    actual = dd.delta
    assert actual == expected


def test_zero_in_days():
    start_date = "1922-01-04"
    end_date = start_date
    dd = DateDifferencer(start_date, end_date, days=True)
    expected = 0
    actual = dd.delta
    assert actual == expected


def test_bad():
    start_date = "1922-01-04"
    end_date = "1901-01-04"
    with pytest.raises(ValueError) as ex:
        DateDifferencer(start_date, end_date, days=False)
    expected = "cannot be"
    assert expected in str(ex.value)


def test_bad_in_days():
    start_date = "1922-01-04"
    end_date = "1901-01-04"
    with pytest.raises(ValueError) as ex:
        DateDifferencer(start_date, end_date, days=True)
    expected = "cannot be"
    assert expected in str(ex.value)


def test_failing_days():
    start_date = "2019-02-23"
    end_date = "today"
    dd = DateDifferencer(start_date, end_date, days=True)
    # print(dd)
