import pytest
from advent_of_code.day1 import first_and_last_digit_combination, _first_digit_or_written_digit

@pytest.mark.parametrize("string, expected_out",[
    ("12", 12),
    ("foo1bar2baz", 12),
    ("1", 11),
    ])
def test_first_and_last_digit(string, expected_out):
    assert first_and_last_digit_combination(string) == expected_out


@pytest.mark.parametrize("string, expected_out",[
    ("12", "1"),
    ("onefoo1bar2baz", "1"),
    ("ztwo1", "2"),
    ])
def test_first_digit_or_written_digit(string, expected_out):
    assert _first_digit_or_written_digit(string) == expected_out
