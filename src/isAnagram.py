from collections import defaultdict
import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dct = defaultdict(int)
        for c in s:
            dct[c] += 1

        for c in t:
            dct[c] -= 1

        for key in dct.keys():
            if dct[key] != 0:
                return False

        return True


cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
]


@pytest.mark.parametrize(
    "s, t, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(s, t, expected):
    actual = Solution().isAnagram(s, t)
    assert actual == expected
