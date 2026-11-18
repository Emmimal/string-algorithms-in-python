import random
from collections import Counter

import pytest

from string_algorithms import first_non_repeating, group_anagrams, is_anagram


@pytest.mark.parametrize('a, b, expected', [
    ('listen', 'silent', True),
    ('rat', 'car', False),
    ('', '', True),
    ('aab', 'abb', False),
    ('abc', 'ab', False),
])
def test_is_anagram(a, b, expected):
    assert is_anagram(a, b) is expected


def test_is_anagram_matches_sorting_on_random_input():
    rng = random.Random(5)
    for _ in range(500):
        a = ''.join(rng.choices('abc', k=rng.randint(0, 6)))
        b = ''.join(rng.choices('abc', k=rng.randint(0, 6)))
        assert is_anagram(a, b) == (sorted(a) == sorted(b))


@pytest.mark.parametrize('text, expected', [
    ('leetcode', 0),
    ('loveleetcode', 2),
    ('aabb', -1),
    ('', -1),
    ('z', 0),
])
def test_first_non_repeating(text, expected):
    assert first_non_repeating(text) == expected


def test_first_non_repeating_matches_brute_force():
    rng = random.Random(9)
    for _ in range(500):
        s = ''.join(rng.choices('abcd', k=rng.randint(0, 10)))
        counts = Counter(s)
        expected = next((i for i, c in enumerate(s) if counts[c] == 1), -1)
        assert first_non_repeating(s) == expected


def test_group_anagrams():
    result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    assert {frozenset(g) for g in result} == {
        frozenset(['eat', 'tea', 'ate']),
        frozenset(['tan', 'nat']),
        frozenset(['bat']),
    }


def test_group_anagrams_empty():
    assert group_anagrams([]) == []
