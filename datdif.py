#! /usr/bin/python3
import argparse
import sys

from datdif import DateDifferencer, get_version

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=f"""\
Calculates and prints the difference between dates. Dates must be in the format YYYY-MM-DD.
The string "today" can be entered for either date.""")

parser.add_argument("start_date", help="starting date")
parser.add_argument("end_date", help="ending date")
parser.add_argument("-v", "--version", action="version", version=f"version={get_version()}", help="show version and exit")
parser.add_argument("--days", action="store_true", help="show result in days")
args = parser.parse_args()

try:
    dd = DateDifferencer(args.start_date, args.end_date, days=args.days)
    print(dd)
except ValueError as ex:
    errmsg = str(ex)
    print(errmsg, file=sys.stderr)
