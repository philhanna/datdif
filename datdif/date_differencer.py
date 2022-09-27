from datetime import datetime, date


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

    def __init__(self, date1, date2, **kwargs):
        """Creates a new DateDifferencer object"""
        self._start_date = DateDifferencer.parse_date(date1)
        self._end_date = DateDifferencer.parse_date(date2)

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    def delta(self):
        """Calculates the difference between two dates"""
        diff = self.end_date - self.start_date
        return diff.days
