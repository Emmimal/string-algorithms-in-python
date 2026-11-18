"""Two pointers on strings: palindrome checks."""


def is_palindrome_simple(s: str) -> bool:
    """Palindrome check for clean input. O(n) time, O(1) extra space."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(s: str) -> bool:
    """Palindrome check that ignores case, spaces, and punctuation.

    O(n) time, O(1) extra space.
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].casefold() != s[right].casefold():
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_short(s: str) -> bool:
    """Shorter version. O(n) time, O(n) extra space."""
    cleaned = [c.casefold() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
