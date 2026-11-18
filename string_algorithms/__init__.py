"""Code for the EmiTechLogic guide: String Algorithms in Python."""
from .concatenation import build_fast, build_slow, edit_with_list
from .frequency import first_non_repeating, group_anagrams, is_anagram
from .prefix import build_vowel_prefix, vowels_in_range
from .problems import (
    is_subsequence,
    is_subsequence_short,
    longest_common_prefix,
    reverse_string,
    reverse_words,
)
from .searching import build_lps, find_all, kmp_search, naive_search, rabin_karp
from .sliding_window import longest_unique_substring
from .two_pointers import is_palindrome, is_palindrome_short, is_palindrome_simple

__all__ = [
    'build_fast', 'build_slow', 'edit_with_list',
    'first_non_repeating', 'group_anagrams', 'is_anagram',
    'build_vowel_prefix', 'vowels_in_range',
    'is_subsequence', 'is_subsequence_short', 'longest_common_prefix',
    'reverse_string', 'reverse_words',
    'build_lps', 'find_all', 'kmp_search', 'naive_search', 'rabin_karp',
    'longest_unique_substring',
    'is_palindrome', 'is_palindrome_short', 'is_palindrome_simple',
]
