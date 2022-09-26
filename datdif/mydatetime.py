from datetime import datetime, timedelta

from datdif import get_max_days


def handle_last_day(method):
    """
    Decorator to preserve the "last day of month" status
    for methods that change the year and/or month.
    If the starting date is the last day of the month in that year
    then the ending date should also be the last day of the
    [new] month in the [new] year, rather than the same date
    """

    def wrapper(*args, **kwargs):
        # Need to get self because this is an instance method
        self: MyDateTime = args[0]
        is_last_day: bool = (get_max_days(self.year, self.month) == self.day)
        method(*args, **kwargs)
        if is_last_day:
            self.day = get_max_days(self.year, self.month)

    return wrapper


class MyDateTime:
    """
    An object containing a year, month, day, hour, minute, and second
    """

    date_format: str = "%Y-%m-%dT%H:%M:%S"

    # ==================================================================
    # Class methods
    # ==================================================================

    @staticmethod
    def delta_difference(start_datetime: datetime,
                         end_datetime: datetime) -> tuple[int, int, int, int]:
        """ Returns the difference between two datetime objects
        as number of days, hours, minutes, and seconds """

        # First count date difference only
        days: int = 0
        dt: datetime = start_datetime
        while dt.date() < end_datetime.date():
            days += 1
            # Add one day to dt
            work = MyDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
            work.add_days(1)
            dt = work.to_date()

        # Now count hours, minutes, seconds
        delta: timedelta = end_datetime - dt
        seconds: int = delta.seconds
        minutes: int = seconds // 60
        seconds -= (minutes * 60)
        hours: int = minutes // 60
        minutes -= (hours * 60)
        return days, hours, minutes, seconds

    @staticmethod
    def delta_to_string(days: int, hours: int, minutes: int, seconds: int):
        """ Returns a number of days, hours, minutes, and seconds
        as a string """
        sb: str = ''
        sb += f'{days} days'
        if hours:
            sb += f', {hours} hours'
        if minutes:
            sb += f', {minutes} minutes'
        if seconds:
            sb += f', {seconds} seconds'
        return sb

    @staticmethod
    def from_date(from_date: datetime):
        """ Converts a date into the fields """
        return MyDateTime(from_date.year,
                          from_date.month,
                          from_date.day,
                          from_date.hour,
                          from_date.minute,
                          from_date.second)

    @staticmethod
    def to_string(*args):
        names: list[str] = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
        outputs: list[str] = []
        for i, value in enumerate(*args):
            if value == 0:
                continue
            name: str = names[i]
            if value == 1:
                string: str = "1 {name}".format(name=name[0:-1])
            else:
                string: str = "{value} {name}".format(value=value, name=name)
            outputs.append(string)
        result: str = ", ".join(outputs)
        if not result:
            return "0"

        # Replace the last comma with "and"
        p: int = result.rfind(',')
        if p > -1:
            prefix: str = result[0:p]
            suffix: str = result[p + 1:]
            result = prefix + " and" + suffix
        return result

    # ==================================================================
    # Instance methods
    # ==================================================================

    def __init__(self,
                 year: int,
                 month: int,
                 day: int,
                 hour: int,
                 minute: int,
                 second: int):
        """ Creates a new MyDateTime from year, month, day, hour, minute, and second """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    @handle_last_day
    def add_years(self, n: int):
        """ Adds the specified number of years to this date """
        self.year += n

    @handle_last_day
    def add_months(self, n: int):
        """ Adds the specified number of months to this date """
        if n > 0:
            for i in range(n):
                self.month += 1
                if self.month > 12:
                    self.year += 1
                    self.month = 1
        elif n < 0:
            for i in range(-n):
                self.month -= 1
                if self.month < 1:
                    self.year -= 1
                    self.month = 12
        else:
            pass

    def add_days(self, n: int):
        """ Adds the specified number of days to this date """
        if n > 0:
            for i in range(n):
                self.day += 1
                if self.day > get_max_days(self.year, self.month):
                    self.add_months(1)
                    self.day = 1
        elif n < 0:
            for i in range(-n):
                self.day -= 1
                if self.day < 1:
                    self.add_months(-1)
                    self.day = get_max_days(self.year, self.month)
        else:
            pass

    def add_hours(self, n: int):
        """ Adds the specified number of hours to this date """
        if n > 0:
            for i in range(n):
                self.hour += 1
                if self.hour > 23:
                    self.add_days(1)
                    self.hour = 0
        elif n < 0:
            for i in range(-n):
                self.hour -= 1
                if self.hour < 0:
                    self.add_days(-1)
                    self.hour = 23
        else:
            pass

    def add_minutes(self, n: int):
        """ Adds the specified number of minutes to this date """
        if n > 0:
            for i in range(n):
                self.minute += 1
                if self.minute > 59:
                    self.add_hours(1)
                    self.minute = 0
        elif n < 0:
            for i in range(-n):
                self.minute -= 1
                if self.minute < 0:
                    self.add_hours(-1)
                    self.minute = 59
        else:
            pass

    def add_seconds(self, n: int):
        """ Adds the specified number of seconds to this date """
        if n > 0:
            for i in range(n):
                self.second += 1
                if self.second > 59:
                    self.add_minutes(1)
                    self.second = 0
        elif n < 0:
            for i in range(-n):
                self.second -= 1
                if self.second < 0:
                    self.add_minutes(-1)
                    self.second = 59
        else:
            pass

    def date_difference(self, other_date: "MyDateTime"):
        """ Returns a tuple with the difference between two dates """
        n_years: int = 0
        n_months: int = 0
        n_days: int = 0
        n_hours: int = 0
        n_minutes: int = 0
        n_seconds: int = 0

        this_date: MyDateTime = MyDateTime(*self.get_fields())

        if this_date == other_date:
            return 0, 0, 0, 0, 0, 0

        if this_date > other_date:
            raise ValueError('End date is past')

        while this_date < other_date:
            new_date: MyDateTime = MyDateTime(*this_date.get_fields())
            new_date.add_years(1)
            if new_date <= other_date:
                n_years += 1
                this_date = new_date
            else:
                break

        while this_date < other_date:
            new_date = MyDateTime(*this_date.get_fields())
            new_date.add_months(1)
            if new_date <= other_date:
                n_months += 1
                this_date = new_date
            else:
                break

        while this_date < other_date:
            new_date = MyDateTime(*this_date.get_fields())
            new_date.add_days(1)
            if new_date <= other_date:
                n_days += 1
                this_date = new_date
            else:
                break

        while this_date < other_date:
            new_date = MyDateTime(*this_date.get_fields())
            new_date.add_hours(1)
            if new_date <= other_date:
                n_hours += 1
                this_date = new_date
            else:
                break

        while this_date < other_date:
            new_date = MyDateTime(*this_date.get_fields())
            new_date.add_minutes(1)
            if new_date <= other_date:
                n_minutes += 1
                this_date = new_date
            else:
                break

        while this_date < other_date:
            new_date = MyDateTime(*this_date.get_fields())
            new_date.add_seconds(1)
            if new_date <= other_date:
                n_seconds += 1
                this_date = new_date
            else:
                break

        return n_years, n_months, n_days, n_hours, n_minutes, n_seconds

    def get_fields(self) -> tuple[int, int, int, int, int, int]:
        """ Returns the year, month, day, hour, minute, and second tuple """
        return self.year, self.month, self.day, self.hour, self.minute, self.second

    def to_date(self) -> datetime:
        """ Converts this object to a datetime """
        return datetime.strptime(str(self), MyDateTime.date_format)

    def __str__(self) -> str:
        return "%04d-%02d-%02dT%02d:%02d:%02d" % self.get_fields()

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other) -> bool:
        return self.year == other.year and \
               self.month == other.month and \
               self.day == other.day and \
               self.hour == other.hour and \
               self.minute == other.minute and \
               self.second == other.second

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.year < other.year:
            return True
        if self.year > other.year:
            return False
        if self.month < other.month:
            return True
        if self.month > other.month:
            return False
        if self.day < other.day:
            return True
        if self.day > other.day:
            return False
        if self.hour < other.hour:
            return True
        if self.hour > other.hour:
            return False
        if self.minute < other.minute:
            return True
        if self.minute > other.minute:
            return False
        if self.second < other.second:
            return True
        if self.second > other.second:
            return False
        return False

    def __gt__(self, other):
        if self.year > other.year:
            return True
        if self.year < other.year:
            return False
        if self.month > other.month:
            return True
        if self.month < other.month:
            return False
        if self.day > other.day:
            return True
        if self.day < other.day:
            return False
        if self.hour > other.hour:
            return True
        if self.hour < other.hour:
            return False
        if self.minute > other.minute:
            return True
        if self.minute < other.minute:
            return False
        if self.second > other.second:
            return True
        if self.second < other.second:
            return False
        return False

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other
