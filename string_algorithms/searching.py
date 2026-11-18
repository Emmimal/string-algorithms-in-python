"""Substring search: naive, find_all, KMP, and Rabin-Karp.

All functions return the start indexes of every match, including overlapping
ones. An empty pattern returns no matches (a deliberate, documented choice).
"""
from collections.abc import Iterator


def naive_search(text: str, pattern: str) -> list[int]:
    """Try every start position. O(n*m) worst case."""
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    matches = []
    for i in range(n - m + 1):
        if text.startswith(pattern, i):
            matches.append(i)
    return matches


def find_all(text: str, pattern: str) -> Iterator[int]:
    """Generator of all (overlapping) matches using str.find and the walrus operator."""
    if not pattern:
        return
    start = 0
    while (index := text.find(pattern, start)) != -1:
        yield index
        start = index + 1


def build_lps(pattern: str) -> list[int]:
    """Longest proper prefix that is also a suffix, for every prefix of pattern."""
    lps = [0] * len(pattern)
    length = 0
    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length
    return lps


def kmp_search(text: str, pattern: str) -> list[int]:
    """Knuth-Morris-Pratt. O(n + m) time, O(m) space."""
    if not pattern:
        return []
    lps = build_lps(pattern)
    matches = []
    j = 0   # how many pattern characters are matched so far
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j - 1]
    return matches


def rabin_karp(text: str, pattern: str, base: int = 256, mod: int = 1_000_000_007) -> list[int]:
    """Rolling-hash search. O(n + m) on average, O(n*m) worst case.

    A matching hash is always confirmed with startswith, so hash collisions
    never produce a wrong answer.
    """
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    high = pow(base, m - 1, mod)   # weight of the leftmost character
    p_hash = t_hash = 0
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text.startswith(pattern, i):
            matches.append(i)
        if i < n - m:   # slide the window one step to the right
            t_hash = ((t_hash - ord(text[i]) * high) * base + ord(text[i + m])) % mod
    return matches
