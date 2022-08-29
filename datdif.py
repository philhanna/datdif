#! /usr/bin/python3
import argparse
from datetime import datetime, date

parser = argparse.ArgumentParser(description=f"""
    Calculates and prints the difference between dates.
    Dates must be in the format MM/DD/YYYY.  The month and day can be
    either one or two digits.  The year must be four digits.
    The string "today" can be entered for either date.
""")

parser.add_argument("start_date", help="Starting date")
parser.add_argument("end_date", help="Ending date")
args = parser.parse_args()

date_format: str = "%m/%d/%Y"
today: date = date.today()


def parse_date(s: str, label: str) -> date:
    if s == "today":
        return today
    try:
        the_date = datetime.strptime(s, date_format).date()
        return the_date
    except ValueError:
        errmsg = f"Invalid {label} date '{s}'"
        raise ValueError(errmsg)


try:
    start_date = parse_date(args.start_date, "start")
    end_date = parse_date(args.end_date, "end")
    diff = end_date - start_date
    days = diff.days
    print(days)
except ValueError as e:
    print(e)
