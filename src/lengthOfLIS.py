from typing import List
import pytest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # O(n^2)解法

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
 

    def lengthOfLIS_rec(self, nums: List[int]) -> int: # O(2^n)解法
        
        def rec(i: int, j: int) -> int:

            if i == len(nums):
                return 0
            
            LIS = rec(i+1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, rec(i+1, i)+1) # include

            return LIS
        
        return rec(0, -1)


    def lengthOfLIS_opt(self, nums: List[int]) -> int: # O(n*log(n))解法

        from bisect import bisect_left
        tails = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)


cases = [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),
    ([1,2,3,4,5,6,7], 7),
    ([7,6,5,4,3,2,1], 1),
]

@pytest.mark.parametrize(
    "nums, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]
)
def test_case(nums, expected):
    actual = Solution().lengthOfLIS_opt(nums)
    assert actual == expected