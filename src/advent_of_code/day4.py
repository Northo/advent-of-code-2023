from dataclasses import dataclass

from advent_of_code.util import get_input_text


@dataclass
class Card:
    id: int
    winning_numbers: list[int]
    present_numbers: list[int]

    @classmethod
    def parse_from_line(cls, line: str):
        """Parse card from input line."""
        # Expected format:
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        # Nb: number of numbers may vary
        assert line.startswith("Card ")
        id_part, numbers_part = line.split(":")
        id = int(id_part[len("Card ") :])

        winning, present = numbers_part.split("|")

        def _to_numbers(string_with_numbers):
            list_with_numbers = [s for s in string_with_numbers.strip().split(" ")]
            # Where there are multiple spaces, we get empty list items.
            # Therefore, skip elements with zero length.
            return [int(number) for number in list_with_numbers if number]

        return Card(
            id=id,
            winning_numbers=_to_numbers(winning),
            present_numbers=_to_numbers(present),
        )


def main():
    lines = get_input_text(4).strip().split("\n")


if __name__ == "__main__":
    main()
