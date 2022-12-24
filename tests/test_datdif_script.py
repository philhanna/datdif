import subprocess

import pytest

from tests import project_root_dir

SCRIPT_NAME = "datdif"


@pytest.fixture
def script():
    script = project_root_dir.joinpath(SCRIPT_NAME)
    return script


def test_no_args(script):
    parms = [script]
    cp = subprocess.run(parms, text=True, capture_output=True)
    actual = cp.stderr
    expected = "arguments are required"
    assert expected in actual


def test_only_start_date(script):
    parms = [script, "2022-12-25"]
    cp = subprocess.run(parms, text=True, capture_output=True)
    actual = cp.stderr
    expected = "end_date"
    assert expected in actual


def test_one_day(script):
    parms = [script, "2022-12-24", "2022-12-25"]
    cp = subprocess.run(parms, text=True, capture_output=True)
    assert cp.returncode == 0
    expected = "1 day"
    actual = cp.stdout.strip()
    assert actual == expected
