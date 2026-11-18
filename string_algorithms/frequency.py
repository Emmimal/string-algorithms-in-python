"""Character frequency counting with dictionaries and Counter."""
from collections import Counter, defaultdict


def is_anagram(a: str, b: str) -> bool:
    """True when both strings use the same characters the same number of times."""
    return len(a) == len(b) and Counter(a) == Counter(b)


def first_non_repeating(s: str) -> int:
    """Index of the first character that appears once, or -1."""
    counts = Counter(s)
    return next((i for i, ch in enumerate(s) if counts[ch] == 1), -1)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other (sorted letters as the key)."""
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        groups[''.join(sorted(word))].append(word)
    return list(groups.values())
