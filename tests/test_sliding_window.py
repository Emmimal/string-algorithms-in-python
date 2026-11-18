import random

import pytest

from string_algorithms import longest_unique_substring


def brute_longest_unique(s: str) -> int:
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


@pytest.mark.parametrize('text, expected', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('', 0),
    ('a', 1),
    ('abba', 2),
    ('dvdf', 3),
])
def test_known_cases(text, expected):
    assert longest_unique_substring(text) == expected


def test_matches_brute_force():
    rng = random.Random(7)
    for _ in range(500):
        s = ''.join(rng.choices('abc', k=rng.randint(0, 12)))
        assert longest_unique_substring(s) == brute_longest_unique(s)
