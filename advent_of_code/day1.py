
from advent_of_code.util import get_input_text

def _first_digit(string: str) -> str:
    return next(filter(str.isdigit, string))

def first_and_last_digit_combination(string: str) -> int:
    return int(
            _first_digit(string)
            + _first_digit(reversed(string)),
            )


def main():
    input_text = get_input_text(1)
    lines = input_text.strip().split("\n")
    answer = sum(
            first_and_last_digit_combination(line) for line in lines
            )
    print(answer)

if __name__ == "__main__":
    main()

