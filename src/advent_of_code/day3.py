import re
from typing import Any

from advent_of_code.util import get_input_text


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


def lines_to_records(lines: str):
    wide_form_records = []
    for i, line in enumerate(lines):
        for record in line_to_records(line):
            wide_form_records.append(record | {"line": i})

    # Make it long-form
    long_form_records = []
    for element_id, record in enumerate(wide_form_records):
        element_width = 1 + record["end_pos"] - record["start_pos"]
        for i in range(element_width):
            long_form_records.append(
                {
                    "element_id": element_id,
                    "line": record["line"],
                    "pos": record["start_pos"] + i,
                    "element": record["element"],
                }
            )
    return long_form_records


# TODO per element that is not a number, search for neighbour element id's
