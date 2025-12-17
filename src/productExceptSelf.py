from typing import List
import pytest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        pre_arr = [1] * len_nums
        su_arr = [1] * len_nums
        res = [None] * len_nums

        for i in range(1, len_nums):
            pre_arr[i] = pre_arr[i - 1] * nums[i - 1]
            su_arr[len_nums - 1 - i] = (
                su_arr[len_nums - 1 - i + 1] * nums[len_nums - 1 - i + 1]
            )

        for i in range(len_nums):
            res[i] = pre_arr[i] * su_arr[i]

        return res


cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
]


@pytest.mark.parametrize(
    "nums, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(nums, expected):
    actual = Solution().productExceptSelf(nums)
    assert actual == expected
