import re
from typing import Any


def line_to_records(line: str) -> list[dict]:
    """Extract all the objects on a line."""
    # \d = digit, \D = non-digit
    parts = re.findall(r"\d+|\D", line)
    character_counter = 0
    objects = []

    for part in parts:
        if part != ".":  # do not add empty elements (Only dots)
            objects.append(
                {
                    "element": part,
                    "start_pos": character_counter,
                    "end_pos": character_counter + len(part) - 1,
                }
            )
        character_counter += len(part)
    return objects


def lines_to_records(lines: list[str]) -> list[dict]:
    wide_form_records = []
    for i, line in enumerate(lines):
        for record in line_to_records(line):
            wide_form_records.append(record | {"line": i})

    # Make it long-form
    long_form_records: list[dict[str, Any]] = []
    for element_id, record in enumerate(wide_form_records):
        element_width = 1 + record["end_pos"] - record["start_pos"]
        long_form_records.extend(
            {
                "element_id": element_id,
                "line": record["line"],
                "pos": record["start_pos"] + i,
                "element": record["element"],
            }
            for i in range(element_width)
        )
    return long_form_records


# TODO per element that is not a number, search for neighbour element id's
def get_neighbouring_positions(pos: int, line: int) -> list[tuple[int, int]]:
    """Per pos line, get a list of all neighbouring positions."""
    left = (pos - 1, line)
    right = (pos + 1, line)
    above_row = ((pos + i, line + 1) for i in (-1, 0, 1))
    below_row = ((pos + i, line - 1) for i in (-1, 0, 1))

    return [left, right, *above_row, *below_row]


def main():
    lines = get_input_text(3).strip().split("\n")
    records = lines_to_records(lines)

    pos_to_element = {(record["pos"], record["line"]): record["element_id"] for record in records}
