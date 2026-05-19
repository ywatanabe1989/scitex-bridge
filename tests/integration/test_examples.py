"""Smoke test: every example script under examples/ runs to completion."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = list(Path(__file__).parents[2].joinpath("examples").glob("*.py"))


def test_examples_directory_contains_example_scripts():
    # Arrange
    # Act
    # Assert
    assert EXAMPLES, "No example scripts found under examples/"


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda p: p.name)
def test_example_script_exits_with_zero_status(example, tmp_path):
    # Arrange
    cmd = [sys.executable, str(example)]
    # Act
    r = subprocess.run(
        cmd,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=60,
    )
    # Assert
    assert r.returncode == 0, (
        f"{example.name} failed:\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}"
    )
