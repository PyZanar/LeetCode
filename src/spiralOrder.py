from typing import List
import pytest

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        steps = [len(matrix[0]), len(matrix) - 1]
        point = [0, -1]
        mode = 0
        while steps[mode%2]:
            
            for i in range(steps[mode%2]):
                point[0] += directions[mode%4][0]
                point[1] += directions[mode%4][1]
                res.append(matrix[point[0]][point[1]])
            steps[mode%2] -= 1
            mode += 1
        return res
    

cases = [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
]

@pytest.mark.parametrize(
    "matrix, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]
)
def test_case(matrix, expected):
    actual = Solution().spiralOrder(matrix)
    assert actual == expected