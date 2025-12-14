from typing import List
import pytest


class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp


cases = [
    (2, [0,1,1]),
    (5, [0,1,1,2,1,2]),
]


@pytest.mark.parametrize(
    "n, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(n, expected):
    actual = Solution().countBits(n)
    assert actual == expected
