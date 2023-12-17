"""Way too overcomplicated solution using a search over Trie trees."""
import functools
from collections.abc import Hashable, Iterable

from advent_of_code.util import get_input_text


def generate_trie_tree(words: Iterable[Iterable[Hashable]]) -> dict:
    """Generate a trie tree structure from a collection of strings.

    See https://en.wikipedia.org/wiki/Trie for background.
    """
    tree: dict[Hashable, dict] = {}
    for word in words:
        functools.reduce(lambda base, el: base.setdefault(el, {}), word, tree)
    return tree


class SequenceNotInTree(Exception):
    """The sequence is not in the tree."""

    ...


def search_tree(tree, sequence):
    node = tree
    for i, element in enumerate(sequence):
        try:
            node = node[element]
        except KeyError:
            raise SequenceNotInTree
        if not node:  # Empty node => leaf node
            return sequence[: i + 1]

    raise SequenceNotInTree


def get_string_to_value():
    all_digit_words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    digits = {str(i): str(i) for i in range(10)}
    return all_digit_words | digits


def get_trie_tree_for_numbers():
    return generate_trie_tree(get_string_to_value())


def find_occurence(tree, sequence):
    for start_position in range(len(sequence)):
        try:
            answer = search_tree(tree, sequence[start_position:])
        except SequenceNotInTree:
            pass
        else:
            return answer
    raise SequenceNotInTree


def main():
    input_text = get_input_text(1)
    lines = input_text.strip().split("\n")

    string_to_value = get_string_to_value()
    tree = generate_trie_tree(get_string_to_value())
    reverse_tree = generate_trie_tree(reversed(element) for element in get_string_to_value())

    answer = sum(
        int(
            string_to_value[find_occurence(tree, line)]
            + string_to_value[find_occurence(reverse_tree, line[::-1])[::-1]]
        )
        for line in lines
    )
    print(answer)


if __name__ == "__main__":
    main()
