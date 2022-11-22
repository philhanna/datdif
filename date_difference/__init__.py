import re

from .maxdays import is_leap_year, get_max_days
from .date_roller import DateRoller
from .date_differencer import DateDifferencer


def get_version():
    import subprocess
    version = None
    cp = subprocess.run(['pip', 'show', __package__], text=True, capture_output=True)
    output = cp.stdout
    for token in output.split('\n'):
        m = re.match(r'^Version: (.*)', token)
        if m:
            version = m.group(1)
            break
    return version


__all__ = [
    'get_version',
    'is_leap_year',
    'get_max_days',
    'DateDifferencer',
    'DateRoller',
]
