from datetime import date

import pytest

from date_difference import DateRoller


@pytest.mark.parametrize("indate,add,expected", [
    ("1997-06-12", 2, "1997-08-12"),  # simple case
    ("1997-06-12", 0, "1997-06-12"),  # zero months
    ("1953-12-04", 3, "1954-03-04"),  # though new year
    ("1954-03-04", -3, "1953-12-04"),  # back though new year
    ("2004-02-29", 3, "2004-05-31"),  # leap date + 3
    ("2004-02-29", -3, "2003-11-30"),  # leap day backwards to previous year
    ("2005-02-28", -12, "2004-02-29"),  # non leap day backwards to previous year
])
def test_add_months(indate, add, expected):
    date_roller = DateRoller(date.fromisoformat(indate))
    date_roller.add_months(add)
    expected = date.fromisoformat(expected)
    actual = date_roller.date
    assert actual == expected
