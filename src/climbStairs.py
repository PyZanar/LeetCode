import pytest

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

cases = [
    (2, 2),
    (3, 3),
]

@pytest.mark.parametrize(
    "n, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]
)
def test_case(n, expected):
    actual = Solution().climbStairs(n)
    assert actual == expected