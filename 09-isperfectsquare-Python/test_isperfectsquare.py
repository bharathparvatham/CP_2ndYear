import pytest
from isperfectsquare import isperfectsquare
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('n, result', [
    ("hello", False),
    (6.25, False),
    (625, True),
    (-625, False),
    (4, True),
    (100, True),
    ("100", False),
])
def test_isperfectsquare(row, result):
    assert isperfectsquare(row) == result
