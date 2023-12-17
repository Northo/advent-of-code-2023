import pytest

from advent_of_code.day1 import (
    SequenceNotInTree,
    find_occurence,
    generate_trie_tree,
    get_trie_tree_for_numbers,
    search_tree,
)


@pytest.mark.parametrize(
    "words, expected_tree",
    [
        (
            ("foo", "bar", "fot"),
            {"f": {"o": {"o": {}, "t": {}}}, "b": {"a": {"r": {}}}},
        ),
        (("1", "2"), {"1": {}, "2": {}}),
    ],
)
def test_generate_tri_tree(words: list[str], expected_tree: dict):
    assert generate_trie_tree(words) == expected_tree


def test_search_tree():
    assert (
        search_tree(
            {"1": {}, "2": {}},
            "1",
        )
        == "1"
    )

    assert (
        search_tree(
            {"1": {"2": {}}, "2": {}},
            "123",
        )
        == "12"
    )

    with pytest.raises(SequenceNotInTree):
        search_tree(
            {"1": {"2": {}}, "2": {}},
            "0123",
        )


def test_tree_search():
    tree = get_trie_tree_for_numbers()
    assert find_occurence(tree, "jaone3two") == "one"
