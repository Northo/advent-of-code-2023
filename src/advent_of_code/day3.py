import re
from typing import Any

import pandas as pd

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


def lines_to_records(lines: list[str]) -> list[dict]:
    wide_form_records: list[dict] = []
    for i, line in enumerate(lines):
        wide_form_records.extend(record | {"line": i} for record in line_to_records(line))

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
    records = get_processed_data()

    # For all the non-numeric entries, find the relevant numbers
    part_positions = records.query("~is_number").index.to_list()
    relevant_neigbouring_positions = get_neigbour_positions(
        part_positions, existing_positions=records.query("is_number").index
    )

    element_ids_per_part = [
        get_element_ids(records, positions) for positions in relevant_neigbouring_positions
    ]
    # Filter to only those where there are two elements
    element_ids_per_part = [
        element_ids for element_ids in element_ids_per_part if len(element_ids) == 2
    ]

    # We now have all the element_ids, time to get the element number and return it
    numeric_element_values = (
        records.query("is_number")[["element_id", "element"]]
        .drop_duplicates()
        .set_index("element_id")["element"]
        .astype(int)
        .to_dict()
    )

    def gear_product_from_elment_ids(element_ids):
        assert len(element_ids) == 2
        return numeric_element_values[element_ids[0]] * numeric_element_values[element_ids[1]]

    answer = sum(gear_product_from_elment_ids(element_ids) for element_ids in element_ids_per_part)
    print(answer)


def get_element_ids(records, indices):
    return records.loc[indices].element_id.unique()


def get_neigbour_positions(part_positions, existing_positions):
    """Per part_position, get a list of neigbours"""
    potential_positions = [get_neighbouring_positions(*position) for position in part_positions]

    def _get_existing(positions):
        return list(set(positions) & set(existing_positions))

    return [_get_existing(positions) for positions in potential_positions]


def get_processed_data():
    lines = get_input_text(3).strip().split("\n")
    records = pd.DataFrame(lines_to_records(lines))
    records["is_number"] = records["element"].str.isnumeric()
    records = records.set_index(["pos", "line"])
    return records


if __name__ == "__main__":
    main()
