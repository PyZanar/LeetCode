from typing import List
import pytest

# 2ポインタ法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
            if height[left] <= height[right]:
                left += 1 
            else:
                right -= 1

        return max_area


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
    ]
)
def test_case(height, expected):
    sol = Solution()
    actual = sol.maxArea(height)
    assert actual == expected