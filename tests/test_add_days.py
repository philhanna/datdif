from datetime import date

import pytest

from date_difference import DateRoller


@pytest.mark.parametrize("indate,add,expected", [
    ("2022-09-26", 0, "2022-09-26"),    # zero days
    ("2022-09-26", 1, "2022-09-27"),    # add one day
    ("2022-09-26", -1, "2022-09-25"),   # subtract one day
    ("2020-02-25", 5, "2020-03-01"),    # past leap month end
    ("2021-02-25", 5, "2021-03-02"),    # past regular month end
    ("1953-12-25", 10, "1954-01-04"),   # past year end
    ("1953-01-01", -1, "1952-12-31"),   # backwards past year start
])
def test_add_days(indate, add, expected):
    start_date = date.fromisoformat(indate)
    date_roller = DateRoller(start_date)
    date_roller.add_days(add)
    expected = date.fromisoformat(expected)
    actual = date_roller.date
    assert actual == expected
