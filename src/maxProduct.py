from typing import List
import pytest

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]
        for num in nums[1:]:
            max_prod, min_prod = max(num*max_prod, num*min_prod, num), min(num*min_prod, num*max_prod, num)
            ans = max(ans, max_prod)
        return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2,3,-2,4], 6),
        ([-2,0,-1], 0),
        ([-2,0,-1, -2], 2),
        ([-4,-3,-2], 12)
    ]
)
def test_case(nums, expected):
    actual = Solution().maxProduct(nums)
    assert actual == expected

