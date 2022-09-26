from datetime import datetime, date


class DateDifferencer:

    @staticmethod
    def date_format():
        return "%m/%d/%Y"

    @staticmethod
    def current_date():
        output = date.today()
        return output

    @staticmethod
    def parse_date(dobj):
        if isinstance(dobj, date):
            return dobj
        if dobj == "today":
            return DateDifferencer.current_date()
        dt = datetime.strptime(dobj, DateDifferencer.date_format())
        the_date = dt.date()
        return the_date

    @staticmethod
    def delta(date1, date2):
        """Calculates the difference between two dates"""
        date1 = DateDifferencer.parse_date(date1)
        date2 = DateDifferencer.parse_date(date2)
        diff = date2 - date1
        return diff.days
