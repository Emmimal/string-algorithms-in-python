"""Modern Python shortcuts for string problems (see the article section).

Needs Python 3.10+ for pairwise and Counter.total(). The batched example
needs Python 3.12+ and is skipped on older versions.
"""
from collections import Counter
from itertools import pairwise

url = 'https://emitechlogic.com/blog'
print(url.removeprefix('https://'))                     # 3.9+
print('report.csv'.removesuffix('.csv'))                # 3.9+
print('Stra\u00dfe'.casefold() == 'STRASSE'.casefold())  # True
print(sum(a == b for a, b in pairwise('aabbbc')))       # 3  (3.10+)
print(Counter('banana').total())                        # 6  (3.10+)

try:
    from itertools import batched
except ImportError:
    print('itertools.batched needs Python 3.12 or newer')
else:
    print([''.join(c) for c in batched('abcdefg', 3)])  # ['abc', 'def', 'g']

# Why lstrip is not removeprefix: strip removes a SET of characters.
print('https://tech.com'.lstrip('https://'))           # ech.com
print('https://tech.com'.removeprefix('https://'))     # tech.com
