import pytest


class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= 1 << i

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res


cases = [
    (1, 2, 3),
    (2, 3, 5),
    (2, -5, -3),
]


@pytest.mark.parametrize(
    "a, b, c", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(a, b, c):
    actual = Solution().getSum(a, b)
    assert actual == c
