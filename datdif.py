#! /usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description=f"""\
Calculates and prints the difference between dates.""")

parser.add_argument("start_date", help="starting date")
parser.add_argument("end_date", help="ending date")
parser.add_argument("--days", action="store_true", help="show result in days")
args = parser.parse_args()
print(f"DEBUG: {args=}")
