import pytest

from string_algorithms import build_fast, build_slow, edit_with_list


def test_build_slow_and_fast_agree():
    parts = ['py', 'thon', ' ', 'rocks']
    assert build_slow(parts) == build_fast(parts) == 'python rocks'


def test_empty_parts():
    assert build_slow([]) == build_fast([]) == ''


def test_strings_are_immutable():
    text = 'hello'
    with pytest.raises(TypeError):
        text[0] = 'H'  # type: ignore[index]


def test_edit_with_list():
    assert edit_with_list('hello', 0, 'H') == 'Hello'
