"""Unit tests for the mainline"""

import subprocess

import pytest


@pytest.fixture
def parms():
    parms = ["python", "-m", "date_difference"]
    return parms


def run(parms):
    return subprocess.run(parms, text=True, capture_output=True)


def test_help(parms):
    parms.append("--help")
    cp = run(parms)
    output = cp.stdout
    assert "usage: datdif [-h]" in output
    errmsg = cp.stderr
    assert errmsg == ""


def test_bad_arg(parms):
    parms.append("--bogus")
    cp = run(parms)
    assert cp.stdout == ""
    assert "error: the following" in cp.stderr


def test_two_days(parms):
    parms.extend(["2020-01-01", "2020-01-03"])
    cp = run(parms)
    expected = "2 days\n"
    actual = cp.stdout
    assert actual == expected


def test_then_to_jfk(parms):
    parms.extend(["1953-12-04", "1963-11-22"])
    cp = run(parms)
    expected = "9 years, 11 months, 18 days\n"
    actual = cp.stdout
    assert actual == expected


def test_backwards(parms):
    parms.extend(["1963-11-22", "1953-12-04"])
    cp = run(parms)
    errmsg = cp.stderr
    assert "cannot be greater" in errmsg


def test_both_today(parms):
    parms.append("today")
    parms.append("today")
    cp = run(parms)
    expected = "0\n"
    actual = cp.stdout
    assert actual == expected


def test_bogus_date(parms):
    parms.append("bogus")
    cp = run(parms)
    actual = cp.stderr
    expected = "arguments are required"
    assert expected in actual
