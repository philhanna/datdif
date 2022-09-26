from .date_differencer import *

from .maxdays import is_leap_year, get_max_days
from .holiday import *
from .mydatetime import MyDateTime


def is_work_day(date_to_check: date) -> bool:
    """ Returns True if the specified date is not a weekend or holiday """
    if is_weekend(date_to_check):
        return False
    if any([x.is_holiday(date_to_check) for x in holidays]):
        return False
    return True


def is_weekend(date_to_check: date):
    day_of_week = date_to_check.weekday()
    return day_of_week in [5, 6]


__all__ = [
    'current_date',
    'date_difference',
    'parse_date',
    'is_leap_year',
    'get_max_days',
    'is_work_day',
    'is_weekend',
    'Holiday',
    'FixedHoliday',
    'FloatingMonday',
    'RelativeHoliday',
    'MyDateTime',
    'NEW_YEARS',
    'MLK_BIRTHDAY',
    'WASHINGTONS_BIRTHDAY',
    'MEMORIAL_DAY',
    'INDEPENDENCE_DAY',
    'LABOR_DAY',
    'COLUMBUS_DAY',
    'VETERANS_DAY',
    'THANKSGIVING',
    'CHRISTMAS',

]
