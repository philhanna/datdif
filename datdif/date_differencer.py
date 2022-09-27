from datetime import datetime, date

from datdif import DateRoller


class DateDifferencer:
    """Calculates the difference between dates"""

    @staticmethod
    def date_format():
        """Returns the date format used by this class"""
        return "%m/%d/%Y"

    @staticmethod
    def current_date():
        """Returns today's date.
        Specified as a method here so that it can be mocked in unit tests"""
        output = date.today()
        return output

    @staticmethod
    def parse_date(dobj):
        """Parses a date string into a date object"""
        if isinstance(dobj, date):
            return dobj
        if dobj == "today":
            return DateDifferencer.current_date()
        dt = datetime.strptime(dobj, DateDifferencer.date_format())
        the_date = dt.date()
        return the_date

    @staticmethod
    def roll_dates(start_date, end_date):
        """Calculates difference between two dates in years, months, and days"""

        roller = DateRoller(start_date)
        n_years = 0
        while roller.date <= end_date:
            start_date = roller.date
            roller.add_years(1)
            n_years += 1
        n_years -= 1

        roller = DateRoller(start_date)
        n_months = 0
        while roller.date <= end_date:
            start_date = roller.date
            roller.add_months(1)
            n_months += 1
        n_months -= 1

        roller = DateRoller(start_date)
        n_days = 0
        while roller.date <= end_date:
            start_date = roller.date
            roller.add_days(1)
            n_days += 1
        n_days -= 1

        return n_years, n_months, n_days

    def __init__(self, date1, date2, days=False):
        """Creates a new DateDifferencer object"""
        self._start_date = DateDifferencer.parse_date(date1)
        self._end_date = DateDifferencer.parse_date(date2)
        if self.start_date > self.end_date:
            raise ValueError("Start date cannot be greater than end date")
        if days:
            self._delta = (self.end_date - self.start_date).days
        else:
            # Calculate years, months, and days
            self._delta = DateDifferencer.roll_dates(self.start_date, self.end_date)

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def delta(self):
        return self._delta

    def __str__(self):
        names: list[str] = ['years', 'months', 'days']
        outputs: list[str] = []
        for i, value in enumerate(self.delta):
            if value == 0:
                continue
            name: str = names[i]
            spart = f"{value} {name}" if value > 1 else f"1 {name[:-1]}"
            outputs.append(spart)
        result = ", ".join(outputs)
        return result if result else "0"
