import pytest

from advent_of_code.day2 import Draw, Game

def test_parse_draw_from_line():
    line = "3 blue, 4 red"
    assert Draw.from_line(line) == Draw(blue=3, red=4)

@pytest.mark.parametrize("line, parsed", [
    (
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        Game(1, [Draw(blue=3, red=4), Draw(red=1, green=2, blue=6), Draw(green=2)]),
    )
])
def test_parse_line(line: str, parsed: Game):
    assert Game.from_line(line) == parsed

def test_is_compatible():
    assert Game(
        1,
        [Draw(red=1)]
    ).is_compatible_with(red=1, green=0, blue=0)

    assert not Game(
        1,
        [Draw(red=10)]
    ).is_compatible_with(red=1, green=0, blue=0)

def test_min_compatible():
    assert Game(
        1,
        [Draw(red=10, green=5), Draw(green=6)]
    ).minimal_compatible_bag() == {
        "red": 10, "green": 6, "blue": 0,
    }