def get_max_days(year: int, month: int) -> int:
    """Returns the maximum number of days in the specified
    month in the specified year"""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    return 29 if is_leap_year(year) else 28


def is_leap_year(year: int) -> bool:
    """Returns True if the specified year is a leap year"""
    if year % 400 == 0:     # e.g., 2000, but not 1900
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
