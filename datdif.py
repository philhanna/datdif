#! /usr/bin/python3
import argparse

from datdif import parse_date

parser = argparse.ArgumentParser(description=f"""\
Calculates and prints the difference between dates.""")

parser.add_argument("start_date", nargs="?", help="starting date")
parser.add_argument("end_date", nargs="?", help="ending date")
parser.add_argument("--days", action="store_true", help="show result in days")
args = parser.parse_args()

date1 = parse_date(args.start_date)