import random

import pytest

from string_algorithms import (
    is_subsequence,
    is_subsequence_short,
    longest_common_prefix,
    reverse_string,
    reverse_words,
)


def test_reverse_string():
    assert reverse_string('algorithm') == 'mhtirogla'
    assert reverse_string('') == ''


def test_reverse_words():
    assert reverse_words('the sky is blue') == 'blue is sky the'
    assert reverse_words('  extra   spaces ') == 'spaces extra'


@pytest.mark.parametrize('s, t, expected', [
    ('ace', 'abcde', True),
    ('aec', 'abcde', False),
    ('', 'abc', True),
    ('abc', '', False),
    ('', '', True),
])
def test_is_subsequence(s, t, expected):
    assert is_subsequence(s, t) is expected
    assert is_subsequence_short(s, t) is expected


def test_subsequence_versions_agree_on_random_input():
    rng = random.Random(21)
    for _ in range(1000):
        s = ''.join(rng.choices('abc', k=rng.randint(0, 5)))
        t = ''.join(rng.choices('abc', k=rng.randint(0, 9)))
        assert is_subsequence(s, t) == is_subsequence_short(s, t)


@pytest.mark.parametrize('words, expected', [
    (['flower', 'flow', 'flight'], 'fl'),
    (['dog', 'racecar'], ''),
    ([], ''),
    (['alone'], 'alone'),
    (['same', 'same'], 'same'),
])
def test_longest_common_prefix(words, expected):
    assert longest_common_prefix(words) == expected
