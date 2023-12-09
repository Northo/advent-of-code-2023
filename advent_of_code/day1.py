import re

from advent_of_code.util import get_input_text

def _first_digit(string: str) -> str:
    return next(filter(str.isdigit, string))

def _first_digit_or_written_digit(string: str) -> str:
    all_digit_words = {'zero': '0',
     'one': '1',
     'two': '2',
     'three': '3',
     'four': '4',
     'five': '5',
     'six': '6',
     'seven': '7',
     'eight': '8',
     'nine': '9'}

    all_digits = (str(i) for i in range(10))
    regex = f"^.*?(({"|".join((*all_digit_words, *all_digits))}))"
    pattern = re.compile(regex)
    digit = pattern.match(string).group(1)
    
    digit = all_digit_words.get(digit, digit)
    return digit
    


def first_and_last_digit_combination(string: str, digit_finder=_first_digit_or_written_digit) -> int:
    return int(
            digit_finder(string)
            + digit_finder(str(reversed(string))),
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

