#! /usr/bin/python3

from datetime import datetime, date

DEFAULT_START_DATE: date = date.today()
DEFAULT_END_DATE: date = date(2038, 8, 21)


def datdif(*dates: list[date]) -> int:
    """ Calculates the difference between two dates. If only one
    date is specified, it is assumed to be the end date,
    and the starting date is today. """
    from_date = 0
    to_date = 0
    nargs = len(dates)
    if nargs == 2:
        from_date = dates[0]
        to_date = dates[1]
    elif nargs == 1:
        from_date = DEFAULT_START_DATE
        to_date = dates[0]
    elif nargs == 0:
        from_date = DEFAULT_START_DATE
        to_date = DEFAULT_END_DATE
    diff = to_date - from_date
    return diff.days


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=f"""
Calculates and prints the difference between dates.
If only one date is specified, it is assumed to be the end date,
and the starting date is today.
If no end date is specified, the default end date {DEFAULT_END_DATE}
will be used.
Dates must be in the format MM/DD/YYYY.  The month and day can be
either one or two digits.  The year must be four digits.
""")
    date_format: str = "%m/%d/%Y"
    today: str = date.strftime(date.today(), date_format)
    parser.add_argument("start_date", nargs="?", default=today, help="Starting date")
    parser.add_argument("end_date", nargs="?", default=datetime.strftime(DEFAULT_END_DATE, date_format), help="Ending date")
    args = parser.parse_args()

    try:
        start_date: date = datetime.strptime(args.start_date, date_format).date()
    except ValueError:
        errmsg = f"Starting date {args.start_date} is not in the format mm/dd/yyyy"
        print(errmsg)
        exit()

    try:
        if args.end_date == "today":
            end_date: date = date.today()
        else:
            end_date: date = datetime.strptime(args.end_date, date_format).date()
    except ValueError:
        errmsg = f"Ending date {args.end_date} is not in the format mm/dd/yyyy"
        print(errmsg)
        exit()

    days = datdif(start_date, end_date)
    print(days)
