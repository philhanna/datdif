import re
from pathlib import Path
from unittest import TestCase

from date_difference import get_version


class TestGetVersion(TestCase):

    def setUp(self):
        self.project_root = Path(__file__).parent.parent

    def test_get_version(self):
        setup_file = self.project_root.joinpath("setup.py")
        with open(setup_file) as fp:
            for line in fp:
                m = re.search("version=(.*),", line)
                if m:
                    strversion = m.group(1)
                    break
        expected = strversion.strip("\'\"")
        actual = get_version()
        self.assertEqual(expected, actual)