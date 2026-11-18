import random

import pytest

from string_algorithms import is_palindrome, is_palindrome_short, is_palindrome_simple


@pytest.mark.parametrize('text, expected', [
    ('level', True),
    ('python', False),
    ('', True),
    ('a', True),
    ('ab', False),
])
def test_simple(text, expected):
    assert is_palindrome_simple(text) is expected


@pytest.mark.parametrize('text, expected', [
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False),
    ('', True),
    ('.,', True),
    ('0P', False),
])
def test_clean_versions(text, expected):
    assert is_palindrome(text) is expected
    assert is_palindrome_short(text) is expected


def test_pointer_and_short_versions_agree_on_random_input():
    rng = random.Random(3)
    for _ in range(1000):
        s = ''.join(rng.choices('aAbB ,.1', k=rng.randint(0, 12)))
        assert is_palindrome(s) == is_palindrome_short(s)
