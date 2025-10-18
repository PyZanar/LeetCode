from typing import List
import pytest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            # aを固定する
            a = nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 以下でb, cを探す
            j, k = i+1, len(nums)-1
            while j < k:
                if a + nums[j] + nums[k] < 0:
                    j += 1
                elif a + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1

                while len(nums)-1 > j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                while i+1 < k < len(nums)-1 and nums[k] == nums[k+1]:
                    k -= 1

        return res
        
        
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]]),
    ]
)
def test_case(nums, expected):
    actual = sorted(Solution().threeSum(nums))
    assert actual == sorted(expected)
