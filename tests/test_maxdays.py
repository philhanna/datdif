import pytest

from date_difference import get_max_days


@pytest.mark.parametrize("year, month, days", [
    (1953, 12, 31),
    (2018, 2, 28),
    (2000, 2, 29),
    (2000, 4, 30),
    (2020, 2, 29),
])
def test_maxdays(year, month, days):
    assert get_max_days(year, month) == days
