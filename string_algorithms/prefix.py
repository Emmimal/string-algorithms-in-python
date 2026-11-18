"""Prefix counts on strings (the prefix sum idea applied to characters)."""
from itertools import accumulate


def build_vowel_prefix(s: str) -> list[int]:
    """prefix[i] = number of vowels in s[:i]. O(n) time and space."""
    is_vowel = (ch.lower() in 'aeiou' for ch in s)
    return list(accumulate(is_vowel, initial=0))


def vowels_in_range(prefix: list[int], left: int, right: int) -> int:
    """Vowels in the inclusive range s[left..right]. O(1) per query."""
    return prefix[right + 1] - prefix[left]
