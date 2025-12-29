from typing import List
from collections import defaultdict
import pytest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


cases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
]


@pytest.mark.parametrize(
    "nums, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(nums, expected):
    actual = Solution().containsDuplicate(nums)
    assert actual == expected
