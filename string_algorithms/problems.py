"""Classic string problems and practice solutions."""


def reverse_string(s: str) -> str:
    """O(n) time and space (a new string is created)."""
    return s[::-1]


def reverse_words(sentence: str) -> str:
    """Reverse the order of the words, keeping each word as is."""
    return ' '.join(sentence.split()[::-1])


def is_subsequence(s: str, t: str) -> bool:
    """Can s be made from t by deleting characters without reordering? O(len(t))."""
    i = 0
    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1
    return i == len(s)


def is_subsequence_short(s: str, t: str) -> bool:
    """Compact version: an iterator remembers its position."""
    it = iter(t)
    return all(ch in it for ch in s)


def longest_common_prefix(strs: list[str]) -> str:
    """Longest starting part shared by all strings."""
    if not strs:
        return ''
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
