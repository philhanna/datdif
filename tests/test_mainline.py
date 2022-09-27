import subprocess
from unittest import TestCase

from tests import project_root_dir


class TestMainline(TestCase):
    """Unit tests for the mainline"""

    def test_help(self):
        parms = ["python", "datdif.py", "--help"]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        output = str(cp.stdout.decode("utf-8"))
        self.assertIn("usage: datdif.py [-h]", output)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertEqual("", errmsg)

    def test_bad_arg(self):
        parms = ["python", "datdif.py", "--version"]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        output = str(cp.stdout.decode("utf-8"))
        self.assertEqual("", output)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("error: the following", errmsg)

    def test_two_days(self):
        parms = ["python", "datdif.py",
                 "1/1/2020",
                 "1/3/2020",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = "2 days\n"
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertEqual("", errmsg)

    def test_then_to_jfk(self):
        parms = ["python", "datdif.py",
                 "12/4/1953",
                 "11/22/1963",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = "9 years, 11 months, 18 days\n"
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertEqual("", errmsg)

    def test_backwards(self):
        parms = ["python", "datdif.py",
                 "11/22/1963",
                 "12/4/1953",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = ""
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("cannot be greater", errmsg)

    def test_missing_arg(self):
        parms = ["python", "datdif.py",
                 "today",
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = ""
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("arguments are required", errmsg)

    def test_bogus_date(self):
        parms = ["python", "datdif.py",
                 "today",
                 "bogus"
                 ]
        cp = subprocess.run(parms, cwd=project_root_dir, capture_output=True)
        expected = ""
        actual = str(cp.stdout.decode("utf-8"))
        self.assertEqual(expected, actual)
        errmsg = str(cp.stderr.decode("utf-8"))
        self.assertIn("is not a valid date", errmsg)
