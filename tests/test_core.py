# tests/test_core.py

import pytest

from fibonacci_kata.core import fibonnaci


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
    ],
)
def test_cases(n, expected):
    assert fibonnaci(n) == expected
