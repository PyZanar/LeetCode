import pytest

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0 # sに含まれる回文の個数

        # 2n-1個の中心に関するループ
        for center in range(2*len(s)-1):
            
            left, right = center//2, center//2 + center%2

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        return count



@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", 3),
        ("aaa", 6),
        ("aabac", 7)
    ]
)
def test_case(s, expected):
    sol = Solution()
    actual = sol.countSubstrings(s)
    assert actual == expected