"""Building strings: why += can be slow and join() is the safe default."""


def build_slow(parts: list[str]) -> str:
    """Build a string with += in a loop.

    In theory this can copy the growing string on every step, so the work
    can grow toward O(n^2). CPython sometimes optimizes it, but Python does
    not guarantee that.
    """
    result = ''
    for part in parts:
        result += part
    return result


def build_fast(parts: list[str]) -> str:
    """Build a string with join(): one pass, linear in the total length."""
    return ''.join(parts)


def edit_with_list(text: str, index: int, new_char: str) -> str:
    """Strings are immutable, so convert to a list, edit, then join."""
    chars = list(text)
    chars[index] = new_char
    return ''.join(chars)
