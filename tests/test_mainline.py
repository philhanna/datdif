import subprocess
from unittest import TestCase


def run(parms):
    return subprocess.run(parms, text=True, capture_output=True)


class TestMainline(TestCase):
    """Unit tests for the mainline"""

    def setUp(self):
        self.parms = ["python", "-m", "date_difference"]

    def test_help(self):
        parms = self.parms
        parms.append("--help")
        cp = run(parms)
        output = cp.stdout
        self.assertIn("usage: datdif [-h]", output)
        errmsg = cp.stderr
        self.assertEqual("", errmsg)

    def test_bad_arg(self):
        parms = self.parms
        parms.append("--bogus")
        cp = run(parms)
        self.assertEqual("", cp.stdout)
        self.assertIn("error: the following", cp.stderr)

    def test_two_days(self):
        parms = self.parms
        parms.extend(["2020-01-01", "2020-01-03"])
        cp = run(parms)
        expected = "2 days\n"
        actual = cp.stdout
        self.assertEqual(expected, actual)

    def test_then_to_jfk(self):
        parms = self.parms
        parms.extend(["1953-12-04", "1963-11-22"])
        cp = run(parms)
        expected = "9 years, 11 months, 18 days\n"
        actual = cp.stdout
        self.assertEqual(expected, actual)

    def test_backwards(self):
        parms = self.parms
        parms.extend(["1963-11-22", "1953-12-04"])
        cp = run(parms)
        errmsg = cp.stderr
        self.assertIn("cannot be greater", errmsg)

    def test_both_today(self):
        parms = self.parms
        parms.append("today")
        parms.append("today")
        cp = run(parms)
        expected = "0\n"
        actual = cp.stdout
        self.assertEqual(expected, actual)

    def test_bogus_date(self):
        parms = self.parms
        parms.append("bogus")
        cp = run(parms)
        actual = cp.stderr
        expected = "arguments are required"
        self.assertIn(expected, actual)