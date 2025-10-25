from typing import List
import pytest

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        prevEnd = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            if prevEnd > interval[0]:
                prevEnd = min(prevEnd, interval[1])
                res += 1
            else:
                prevEnd = interval[1]

        return res

@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2),
    ]
)
def test_case(intervals, expected):
    actual = Solution().eraseOverlapIntervals(intervals)
    assert actual == expected