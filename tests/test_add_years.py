from datetime import date

import pytest

from date_difference import DateRoller


@pytest.mark.parametrize("indate,years_to_add,expected", [
    ("2020-02-29", 1, "2021-02-28"),  # Add one year to leap day
    ("2020-02-29", 4, "2024-02-29"),  # Add four years to leap day
    ("2020-02-15", 4, "2024-02-15"),  # Add four years to non-leap day
    ("1953-12-04", -1, "1952-12-04"),  # Negative years
    ("2020-02-29", -3, "2017-02-28"),  # Negative years on leap day
    ("1904-02-29", -4, "1900-02-28"),  # Negative years on leap day from 1904
])
def test_add_years(indate, years_to_add, expected):
    indate = date.fromisoformat(indate)
    expected = date.fromisoformat(expected)
    date_roller = DateRoller(indate)
    date_roller.add_years(years_to_add)
    actual = date_roller.date
    assert actual == expected
