import pytest
from removeduplicate import removeduplicate
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('a, result', [
    ("JavaPython", "JavPython"), ("HelloWorld", "HeloWrd"), ("EEE", "E"),
    ("a a ", "a "), ("121212121", "12"), ("", ""),
    ("Test", "Test"), ("1001", "10"), ("11110000", "10"),
])
def test_removeduplicate(a, result):
    assert removeduplicate(a) == result
