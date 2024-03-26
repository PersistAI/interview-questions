import pytest
from questions import two_sum, is_valid_parenthesis

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])

def test_two_sum(nums, target, expected):
    assert sorted(two_sum(nums, target)) == sorted(expected)

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
])
def test_is_valid(s, expected):
    assert is_valid_parenthesis(s) == expected
