import pytest
from nthwithproperty309 import nthwithproperty309
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, result', [
    (0, 309),
    (1, 418),
    (2, 462),
    (3, 474),
    (4, 575),
    (5, 635),
    (6, 662),
    (100, 2014),
    (1000, 7813)
])
def test_nthwithproperty309(x, result):
    assert nthwithproperty309(x) == result
