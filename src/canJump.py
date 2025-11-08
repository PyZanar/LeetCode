from typing import List
import pytest

class Solution:
    def canJump_brute(self, nums: List[int]) -> bool:
        memo = {}
        def rec(i: int) -> bool:

            if i == len(nums)-1:
                return True
            if i in memo:
                return memo[i]
            
            ret = False
            for jump in range(1, nums[i]+1):
                ret = ret or rec(i+jump)
            memo[i] = ret
            return memo[i]
        
        return rec(0)

    def canJump(self, nums: List[int]) -> bool:
        zeroCtr = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= zeroCtr:
                zeroCtr += 1
            else:
                zeroCtr = 0
                
        return True if zeroCtr == 0 else False


cases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([4,3,2,1,0,1], False),
    ([1,1,1,1,1], True),
    ([1,3,0,0,1], True),
    ([0,1,2,3,4], False),
    ([3,0,8,2,0,0,1], True)
]

@pytest.mark.parametrize(
    "nums, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]
)
def test_case(nums, expected):
    actual = Solution().canJump(nums)
    assert actual == expected