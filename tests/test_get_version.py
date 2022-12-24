import re

from date_difference import get_version
from tests import project_root_dir


def test_get_version():
    setup_file = project_root_dir.joinpath("setup.py")
    data = setup_file.read_text()
    strversion = ""
    for line in data.splitlines():
        m = re.search(r"version\s*=\s*(.*),", line)
        if m:
            strversion = m.group(1)
            break
    expected = strversion.strip("\'\"")
    actual = get_version()
    if actual is not None:
        assert actual == expected
