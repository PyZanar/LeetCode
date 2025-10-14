from typing import List
import pytest

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # ピボットを見つける
        pos = len(nums) - 1
        while pos >= 1 and nums[pos-1] >= nums[pos]:
            pos -= 1
        if not pos == 0:
            pos_pivot = pos - 1
        else:
            nums.sort()
            return

        # ピボットとswapする
        pos = len(nums) - 1
        while nums[pos] <= nums[pos_pivot]:
            pos -= 1
        nums[pos_pivot], nums[pos] = nums[pos], nums[pos_pivot]

        # ピボットより右側をソートする
        nums[pos_pivot+1:] = reversed(nums[pos_pivot+1:])
        

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1], [1])
    ]
)
def test_case(nums, expected):
    sol = Solution()
    sol.nextPermutation(nums)
    assert nums == expected