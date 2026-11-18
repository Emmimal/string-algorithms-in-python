"""Sliding window on strings."""


def longest_unique_substring(s: str) -> int:
    """Length of the longest substring without repeating characters.

    O(n) time. O(k) space for k distinct characters.
    """
    last_seen: dict[str, int] = {}   # character -> most recent index
    left = best = 0
    for right, ch in enumerate(s):
        left = max(left, last_seen.get(ch, -1) + 1)
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
