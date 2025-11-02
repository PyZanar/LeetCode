import pytest

class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2,len(s)+1):
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]

cases = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
]

@pytest.mark.parametrize(
    "s, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]
)
def test_case(s, expected):
    actual = Solution().numDecodings(s)
    assert actual == expected