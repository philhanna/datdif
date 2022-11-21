import re
import subprocess

from .maxdays import is_leap_year, get_max_days
from .date_roller import DateRoller
from .date_differencer import DateDifferencer

pkgname = 'datdif'  # Change this to the desired package name


def get_version():
    version = None
    parms = ['pip', 'show', pkgname]
    cp = subprocess.run(
        parms,
        capture_output=True,
        check=True,
        text=True
    )
    for token in cp.stdout.splitlines():
        m = re.match(r'^Version:\s+(.*)', token)
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
