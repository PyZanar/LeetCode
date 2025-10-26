from typing import List
import pytest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if lastEnd >= start:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output


@pytest.mark.parametrize(
    "intervals, expected_list",
    [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[4,7],[1,4]], [[1,7]]),
        ([[1,7],[2,5]], [[1,7]]),
    ]
)
def test_case(intervals, expected_list):
    actual = sorted(Solution().merge(intervals), key=lambda x: x[0])
    expected = sorted(expected_list, key=lambda x: x[0])
    assert actual == expected