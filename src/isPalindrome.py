import pytest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for i in range(len(s)):
            if s[i].isalnum():
                newStr += s[i].lower()
           
        return newStr == newStr[::-1]


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("Was it a car or a cat I saw?", True),
        ("tab a cat", False),
        (" ", True),
    ]
)
def test_case(s, expected):
    actual = Solution().isPalindrome(s)
    assert actual == expected