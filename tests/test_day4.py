import pytest

from advent_of_code.day4 import Card


@pytest.mark.parametrize(
    ("line", "expected_card"),
    [
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            Card(
                id=1,
                winning_numbers=[41, 48, 83, 86, 17],
                present_numbers=[83, 86, 6, 31, 17, 9, 48, 53],
            ),
        ),
        (
            "Card 100: 31 18  3  6 72 | 77 10 23 35 67 36 11",
            Card(
                id=100,
                winning_numbers=[31, 18, 3, 6, 72],
                present_numbers=[77, 10, 23, 35, 67, 36, 11],
            ),
        ),
    ],
)
def test_parse_card_from_line(line: str, expected_card: Card):
    assert expected_card == Card.parse_from_line(line)


@pytest.mark.parametrize(
    ("card", "points"),
    [
        (Card(id=0, winning_numbers=[11, 22, 33], present_numbers=[0, 11]), 1),
        (Card(id=0, winning_numbers=[11, 22, 33], present_numbers=[0]), 0),
        (Card(id=0, winning_numbers=[11, 22, 33], present_numbers=[0, 11, 22, 33]), 4),
    ],
)
def test_card_points(card: Card, points: int):
    assert card.points == points
