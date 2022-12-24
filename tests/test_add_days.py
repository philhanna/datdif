from datetime import date

from date_difference import DateRoller


def test_add_zero_days():
    start_date = date(2022, 9, 26)
    date_roller = DateRoller(start_date)
    date_roller.add_days(0)
    expected = start_date
    actual = date_roller.date
    assert actual == expected


def test_add_1_day():
    start_date = date(2022, 9, 26)
    date_roller = DateRoller(start_date)
    date_roller.add_days(1)
    expected = date(2022, 9, 27)
    actual = date_roller.date
    assert actual == expected


def test_subtract_1_day():
    start_date = date(2022, 9, 26)
    date_roller = DateRoller(start_date)
    date_roller.add_days(-1)
    expected = date(2022, 9, 25)
    actual = date_roller.date
    assert actual == expected


def test_past_leap_month_end():
    start_date = date(2020, 2, 25)
    date_roller = DateRoller(start_date)
    date_roller.add_days(5)
    expected = date(2020, 3, 1)
    actual = date_roller.date
    assert actual == expected


def test_past_regular_month_end():
    start_date = date(2021, 2, 25)
    date_roller = DateRoller(start_date)
    date_roller.add_days(5)
    expected = date(2021, 3, 2)
    actual = date_roller.date
    assert actual == expected


def test_past_year_end():
    start_date = date(1953, 12, 25)
    date_roller = DateRoller(start_date)
    date_roller.add_days(10)
    expected = date(1954, 1, 4)
    actual = date_roller.date
    assert actual == expected


def test_past_year_start():
    start_date = date(1953, 1, 1)
    date_roller = DateRoller(start_date)
    date_roller.add_days(-1)
    expected = date(1952, 12, 31)
    actual = date_roller.date
    assert actual == expected
