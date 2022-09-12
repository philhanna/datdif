from datetime import datetime, date


def date_format():
    return "%m/%d/%Y"


def current_date():
    output = date.today()
    return output


def parse_date(dobj):
    if isinstance(dobj, date):
        return dobj
    if dobj == "today":
        return current_date()
    dt = datetime.strptime(dobj, date_format())
    the_date = dt.date()
    return the_date


def date_difference(date1, date2):
    """Calculates the difference between two dates"""
    date1 = parse_date(date1)
    date2 = parse_date(date2)
    diff = date2 - date1
    return diff.days
