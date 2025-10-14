from typing import List
import pytest
import sys

sys.setrecursionlimit(10**6)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_reachable, atlantic_reachable = set(), set()
        both_reachable = []

        def dfs(r: int, c: int, visited: set, prev_height: int) -> None:
            # 範囲外チェック
            if not ((0 <= r < len(heights)) and (0 <= c < len(heights[0]))):
                return 

            # すでに訪問済みなら return
            if (r, c) in visited:
                return

            # 今の高さ < prev_height なら return
            if heights[r][c] < prev_height:
                return

            # 訪問登録してから上下左右に再帰
            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

        r = 0
        for c in range(len(heights[0])):
            dfs(0, c, pacific_reachable, heights[0][c])

        c = 0
        for r in range(len(heights)):
            dfs(r, 0, pacific_reachable, heights[r][0])

        r = len(heights)-1
        for c in range(len(heights[0])):
            dfs(r, c, atlantic_reachable, heights[r][c])

        c = len(heights[0])-1
        for r in range(len(heights)):
            dfs(r, c, atlantic_reachable, heights[r][c])

        # return list(pacific_reachable & atlantic_reachable)
        return [list(element) for element in pacific_reachable & atlantic_reachable]

        

@pytest.mark.parametrize(
    "heights, expected",
    [
        ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], 
         [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),

        ([[1]], [[0, 0]]),
    ]
)
def test_case(heights, expected):
    actual_list = sorted(Solution().pacificAtlantic(heights))
    assert actual_list == expected