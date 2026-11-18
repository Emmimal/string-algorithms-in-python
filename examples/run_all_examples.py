"""Run every example from the article and print the results.

Usage (from the repository root):
    python examples/run_all_examples.py
"""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from string_algorithms import (  # noqa: E402
    build_lps, build_vowel_prefix, edit_with_list, find_all, first_non_repeating,
    group_anagrams, is_anagram, is_palindrome, is_palindrome_short,
    is_palindrome_simple, is_subsequence, is_subsequence_short, kmp_search,
    longest_common_prefix, longest_unique_substring, naive_search, rabin_karp,
    reverse_string, reverse_words, vowels_in_range,
)


def section(title: str) -> None:
    print(f'\n== {title} ==')


section('How strings work')
text = 'python'
print(text[0], text[-1], text[1:4], len(text))
print(len('cafe'), len('cafe\u0301'))

section('Immutability')
print(edit_with_list('hello', 0, 'H'))

section('Patterns')
print(is_palindrome_simple('level'), is_palindrome_simple('python'))
print(Counter('banana'))
prefix = build_vowel_prefix('education')
print(prefix, vowels_in_range(prefix, 2, 5))

section('Common problems')
print(reverse_string('algorithm'), '|', reverse_words('the sky is blue'))
print(is_palindrome('A man, a plan, a canal: Panama'), is_palindrome('race a car'), is_palindrome(''))
print(is_palindrome_short('A man, a plan, a canal: Panama'))
print(is_anagram('listen', 'silent'), is_anagram('rat', 'car'))
print(first_non_repeating('leetcode'), first_non_repeating('aabb'))
print(longest_unique_substring('abcabcbb'), longest_unique_substring('pwwkew'), longest_unique_substring(''))
print(naive_search('ababcabab', 'abab'))

section('KMP and Rabin-Karp')
print(build_lps('abab'), kmp_search('ababcabab', 'abab'))
print(rabin_karp('ababcabab', 'abab'))
print(list(find_all('aaaa', 'aa')))

section('Practice problems')
print(is_subsequence('ace', 'abcde'), is_subsequence('aec', 'abcde'))
print(is_subsequence_short('ace', 'abcde'), is_subsequence_short('aec', 'abcde'))
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(longest_common_prefix(['flower', 'flow', 'flight']), repr(longest_common_prefix(['dog', 'racecar'])))
