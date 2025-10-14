import pytest

class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for _ in range(32):
            res = res << 1
            res += n & 1
            n = n >> 1

        return res

@pytest.mark.parametrize(
    "n, expected",
    [
        (43261596, 964176192),
        (2147483644, 1073741822),
    ]
)
def test_case(n, expected):
    actual = Solution().reverseBits(n)
    assert actual == expected