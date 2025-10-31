from typing import List
import pytest

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        idx_tmp = 0

        for interval in intervals:
            
            if interval[1] < newInterval[0]:
                output.append(interval)
                idx_tmp += 1
            else:
                break

        idx_tmp2 = idx_tmp
        for interval in intervals[idx_tmp:]:
            
            if newInterval[1] >= interval[0]:
                idx_tmp2 += 1
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            else:
                output.extend([newInterval]+intervals[idx_tmp2:])
                break
        else:
            output.append(newInterval)

        return output
            

cases = [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
    ([[1,3],[4,6]], [2,5], [[1,6]]),
    ( [[1,2],[3,5],[9,10]], [6,7], [[1,2],[3,5],[6,7],[9,10]])
]

@pytest.mark.parametrize(
    "intervals, newInterval, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]
)
def test_case(intervals, newInterval, expected):
    actual = Solution().insert(intervals, newInterval)
    assert actual == expected