from abc import ABC, abstractmethod
from datetime import datetime, date
from datdif import get_max_days


class Holiday(ABC):
    """ Base class for several holiday types.
        Source: https://en.wikipedia.org/wiki/Federal_holidays_in_the_United_States
    """

    @abstractmethod
    def is_holiday(self, date_to_check: date) -> bool:
        """ Returns True if the specified date is a holiday """
        pass


class FixedHoliday(Holiday):
    """ A holiday that occurs on a specific day of a specific month
    (like Christmas) """

    def __init__(self, month: int, day: int):
        super().__init__()
        self.month: int = month
        self.day: int = day

    def is_holiday(self, date_to_check: datetime.date) -> bool:
        return date_to_check.month == self.month and date_to_check.day == self.day


class FloatingMonday(Holiday):
    """ A holiday that falls on the first Monday on or after
    the specified fixed month/day
    """

    def __init__(self, month: int, day: int):
        super().__init__()
        self.month: int = month
        self.day: int = day

    def is_holiday(self, date_to_check: date) -> bool:
        if date_to_check.month != self.month:
            return False
        tempdate: date = date(date_to_check.year, self.month, self.day)
        limit: int = get_max_days(tempdate.year, tempdate.month)
        # Add days to temp date until either:
        #     It's a monday
        #     It's past the end of the month
        while True:
            if tempdate.day > limit:
                return False
            if tempdate.weekday() == 0:  # Monday
                return tempdate == date_to_check
            tempdate = date(tempdate.year, tempdate.month, tempdate.day + 1)


class RelativeHoliday(Holiday):
    """ A holiday that occurs on the nth instance of a specific day of the week in a month
        (like Thanksgiving, the 4th Thursday in November)
    """
    LAST: int = -1

    def __init__(self, ordinal: int, day_of_week: int, month: int):
        super().__init__()
        if ordinal < -1:
            raise ValueError('Ordinal must 1, 2, ... for first, second, or RelativeHoliday.LAST')

        self.ordinal: int = ordinal
        if day_of_week < 0 or day_of_week > 6:
            raise ValueError(f'Day of week must be between 0-Monday through 6-Sunday, not {day_of_week}')
        self.day_of_week: int = day_of_week
        self.month: int = month

    def is_holiday(self, date_to_check: datetime.date) -> bool:

        # Is not this holiday if not the same month
        if date_to_check.month != self.month:
            return False

        # Make a list of the 1st, 2nd, ..., last instance of that day_of_week in the month
        tempdate: date = date(date_to_check.year, date_to_check.month, 1)

        # Starting from the first of the specified month, find the first day
        # that is of the specified weekday (0=Monday, 1=Tuesday, etc.)
        while tempdate.weekday() != self.day_of_week:
            tempdate: date = date(tempdate.year, tempdate.month, tempdate.day + 1)

        # Start creating a list of the first, second, ... instance of that day
        # of the week in that month
        limit: int = get_max_days(tempdate.year, tempdate.month)
        a_list: list[date] = []
        while True:
            a_list.append(tempdate)
            new_day: int = tempdate.day + 7
            if new_day > limit:
                break
            tempdate = date(tempdate.year, tempdate.month, new_day)

        # Now check to see whether this date matches
        if self.ordinal == RelativeHoliday.LAST:
            return date_to_check == a_list[-1]

        for i in range(len(a_list)):
            if self.ordinal - 1 == i:
                return date_to_check == a_list[i]

        # Nope
        return False


NEW_YEARS = FixedHoliday(1, 1)
MLK_BIRTHDAY = FloatingMonday(1, 15)
WASHINGTONS_BIRTHDAY = FloatingMonday(2, 15)
MEMORIAL_DAY = RelativeHoliday(RelativeHoliday.LAST, 0, 5)
INDEPENDENCE_DAY = FixedHoliday(7, 4)
LABOR_DAY = RelativeHoliday(1, 0, 9)
COLUMBUS_DAY = RelativeHoliday(2, 0, 10)
VETERANS_DAY = FixedHoliday(11, 11)
THANKSGIVING = RelativeHoliday(4, 3, 11)
CHRISTMAS = FixedHoliday(12, 25)

holidays = [
    NEW_YEARS,
    MLK_BIRTHDAY,
    WASHINGTONS_BIRTHDAY,
    MEMORIAL_DAY,
    INDEPENDENCE_DAY,
    LABOR_DAY,
    COLUMBUS_DAY,
    VETERANS_DAY,
    THANKSGIVING,
    CHRISTMAS,
]
