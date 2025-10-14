from typing import List
import pytest

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums_set = set(nums)
        max_len = 1

        for num in nums_set:
            if num-1 not in nums_set: # numが連続列の起点になりうる
                curr = num + 1
                while curr in nums_set:
                    curr += 1
                max_len = max(max_len, curr-num)

        return max_len

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,0,1,2], 3),
        ([], 0)
    ]
)
def test_case(nums, expected):
    sol = Solution()
    actual = sol.longestConsecutive(nums)
    assert actual == expected