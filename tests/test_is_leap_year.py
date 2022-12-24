import pytest

from date_difference import is_leap_year


@pytest.mark.parametrize("year", [
    2000,
    2020,
    3004,
])
def test_is_leap_year(year):
    assert is_leap_year(year)


@pytest.mark.parametrize("year", [
    2001,
    2018,
    1900,
    3000,
])
def test_is_not_leap_year(year):
    assert not is_leap_year(year)
