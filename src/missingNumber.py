from typing import List
import pytest

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        for num in nums:
            if num != n:
                return n
            n += 1
            
        return len(nums)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3,0,1], 2),
        ([0,1], 2),
        ([9,6,4,2,3,5,7,0,1], 8)
    ]
)
def test_case(nums, expected):
    sol = Solution()
    actual = sol.missingNumber(nums)
    assert actual == expected