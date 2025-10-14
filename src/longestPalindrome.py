import pytest

class Solution:
    def longestPalindrome(self, s: str) -> str:

        start, end = 0, 0

        # 2n-1個の中心に関するループ
        for center in range(2*len(s)-1):

            left = center // 2
            right = left + center % 2

            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                if right - left > end - start:
                    start, end = left, right

                left, right = left - 1, right + 1
            
        return s[start:end+1]


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"])
    ]
)
def test_case(s, expected):
    sol = Solution()
    actual = sol.longestPalindrome(s)
    assert actual in expected