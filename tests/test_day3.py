import pytest

from advent_of_code.day3 import line_to_records, lines_to_records


@pytest.mark.parametrize(
    "line, records",
    [
        (
            "467..114..",
            [
                {"element": "467", "start_pos": 0, "end_pos": 2},
                {"element": "114", "start_pos": 5, "end_pos": 7},
            ],
        ),
        (
            "467....*..",
            [
                {"element": "467", "start_pos": 0, "end_pos": 2},
                {"element": "*", "start_pos": 7, "end_pos": 7},
            ],
        ),
        (
            "467$...*..",
            [
                {"element": "467", "start_pos": 0, "end_pos": 2},
                {"element": "$", "start_pos": 3, "end_pos": 3},
                {"element": "*", "start_pos": 7, "end_pos": 7},
            ],
        ),
    ],
)
def test_line_to_records(line: str, records: list[dict]):
    assert line_to_records(line) == records


def test_lines_to_records():
    lines = ["467..114..", "467....*.."]
    records = lines_to_records(lines)

    assert records == [
        {"element_id": 0, "pos": 0, "line": 0, "element": "467"},
        {"element_id": 0, "pos": 1, "line": 0, "element": "467"},
        {"element_id": 0, "pos": 2, "line": 0, "element": "467"},
        {"element_id": 1, "pos": 5, "line": 0, "element": "114"},
        {"element_id": 1, "pos": 6, "line": 0, "element": "114"},
        {"element_id": 1, "pos": 7, "line": 0, "element": "114"},
        {"element_id": 2, "pos": 0, "line": 1, "element": "467"},
        {"element_id": 2, "pos": 1, "line": 1, "element": "467"},
        {"element_id": 2, "pos": 2, "line": 1, "element": "467"},
        {"element_id": 3, "pos": 7, "line": 1, "element": "*"},
    ]
