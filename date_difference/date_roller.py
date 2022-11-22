from datetime import date

from date_difference import get_max_days


def handle_last_day(method):
    """Decorator to preserve the "last day of month" status
    for methods that change the year and/or month.
    If the starting date is the last day of the month in that year
    then the ending date should also be the last day of the
    [new] month in the [new] year, rather than the same date.
    """

    def wrapper(*args, **kwargs):
        # Need to get self because this is an instance method
        self: DateRoller = args[0]
        is_last_day: bool = get_max_days(self.year, self.month) == self.day
        method(*args, **kwargs)
        if is_last_day:
            self.day = get_max_days(self.year, self.month)
    return wrapper


class DateRoller:
    """Utility class for adding years, months, and/or days to a date"""

    def __init__(self, date: date):
        self._year = date.year
        self._month = date.month
        self._day = date.day

    @property
    def date(self):
        return date(self.year, self.month, self.day)

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, new_year: int):
        self._year = new_year

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, new_month: int):
        self._month = new_month

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, new_day: int):
        self._day = new_day

    ####################################################################
    #   Methods to add or subtract time units
    ####################################################################

    @handle_last_day
    def add_years(self, n: int):
        """Adds the specified number of years to this date"""
        self.year += n

    @handle_last_day
    def add_months(self, n: int):
        """Adds the specified number of months to this date"""
        if n > 0:
            for i in range(n):
                self.month += 1
                if self.month > 12:
                    self.year += 1
                    self.month = 1
        elif n < 0:
            n = -n
            for i in range(n):
                self.month -= 1
                if self.month < 1:
                    self.year -= 1
                    self.month = 12

    def add_days(self, n: int):
        """Adds the specified number of days to this date"""
        if n > 0:
            for i in range(n):
                self.day += 1
                if self.day > get_max_days(self.year, self.month):
                    self.add_months(1)
                    self.day = 1
        elif n < 0:
            n = -n
            for i in range(n):
                self.day -= 1
                if self.day < 1:
                    self.add_months(-1)
                    self.day = get_max_days(self.year, self.month)


