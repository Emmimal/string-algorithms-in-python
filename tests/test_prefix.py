import random

from string_algorithms import build_vowel_prefix, vowels_in_range


def test_article_example():
    prefix = build_vowel_prefix('education')
    assert prefix == [0, 1, 1, 2, 2, 3, 3, 4, 5, 5]
    assert vowels_in_range(prefix, 2, 5) == 2


def test_empty_string():
    assert build_vowel_prefix('') == [0]


def test_uppercase_vowels_count():
    prefix = build_vowel_prefix('AEIOU')
    assert vowels_in_range(prefix, 0, 4) == 5


def test_matches_direct_counting():
    rng = random.Random(13)
    for _ in range(300):
        s = ''.join(rng.choices('abcdeiouAEXY', k=rng.randint(1, 15)))
        prefix = build_vowel_prefix(s)
        left = rng.randint(0, len(s) - 1)
        right = rng.randint(left, len(s) - 1)
        direct = sum(ch.lower() in 'aeiou' for ch in s[left:right + 1])
        assert vowels_in_range(prefix, left, right) == direct
