import subprocess
from unittest import TestCase

from tests import project_root_dir


class TestMainline(TestCase):
    """Unit tests for the mainline"""

    def test_help(self):
        parms = ["python", "date_difference.py", "--help"]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        output = str(cp.stdout.decode("utf-8"))
        self.assertIn("usage: date_difference.py [-h]", output)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertEqual("", errmsg)

    def test_bad_arg(self):
        parms = ["python", "date_difference.py", "--bogus"]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        output = str(cp.stdout.decode("utf-8"))
        self.assertEqual("", output)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("error: the following", errmsg)

    def test_two_days(self):
        parms = ["python", "date_difference.py", "2020-01-01", "2020-01-03"]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = "2 days\n"
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertEqual("", errmsg)

    def test_then_to_jfk(self):
        parms = ["python", "date_difference.py",
                 "1953-12-04",
                 "1963-11-22",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = "9 years, 11 months, 18 days\n"
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertEqual("", errmsg)

    def test_backwards(self):
        parms = ["python", "date_difference.py",
                 "1963-11-22",
                 "1953-12-04",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = ""
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("cannot be greater", errmsg)

    def test_missing_arg(self):
        parms = ["python", "date_difference.py",
                 "today",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = ""
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("arguments are required", errmsg)

    def test_bogus_date(self):
        parms = ["python", "date_difference.py",
                 "today",
                 "bogus"
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = ""
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("is not a valid date", errmsg)
