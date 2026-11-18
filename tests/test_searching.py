import random

import pytest

from string_algorithms import build_lps, find_all, kmp_search, naive_search, rabin_karp

SEARCHERS = [naive_search, kmp_search, rabin_karp, lambda t, p: list(find_all(t, p))]


@pytest.mark.parametrize('search', SEARCHERS)
@pytest.mark.parametrize('text, pattern, expected', [
    ('ababcabab', 'abab', [0, 5]),
    ('aaaa', 'aa', [0, 1, 2]),           # overlapping matches
    ('hello', 'xyz', []),
    ('hello', 'hello', [0]),
    ('hi', 'hello', []),                  # pattern longer than text
    ('', 'a', []),
    ('abc', '', []),                      # empty pattern returns no matches
    ('abcabc', 'c', [2, 5]),
])
def test_known_cases(search, text, pattern, expected):
    assert search(text, pattern) == expected


@pytest.mark.parametrize('pattern, expected', [
    ('abab', [0, 0, 1, 2]),
    ('aaaa', [0, 1, 2, 3]),
    ('abcabc', [0, 0, 0, 1, 2, 3]),
    ('aabaaab', [0, 1, 0, 1, 2, 2, 3]),
    ('a', [0]),
    ('', []),
])
def test_build_lps(pattern, expected):
    assert build_lps(pattern) == expected


def test_all_algorithms_agree_on_random_input():
    rng = random.Random(11)
    for _ in range(1000):
        text = ''.join(rng.choices('ab', k=rng.randint(0, 15)))
        pattern = ''.join(rng.choices('ab', k=rng.randint(1, 4)))
        expected = naive_search(text, pattern)
        assert kmp_search(text, pattern) == expected
        assert rabin_karp(text, pattern) == expected
        assert list(find_all(text, pattern)) == expected


def test_unicode_text():
    text = 'h\u00e9llo w\u00f6rld \u2603 hello \u2603'
    for pattern in ['\u2603', 'w\u00f6rld', 'hello', 'xyz']:
        expected = naive_search(text, pattern)
        assert kmp_search(text, pattern) == expected
        assert rabin_karp(text, pattern) == expected
