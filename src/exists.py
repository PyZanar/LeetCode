from typing import List
import pytest

class Solution:
    def exist1(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(row, col, curr_idx, visited):

            isExists = False

            if curr_idx == 0 and word[0] != board[row][col]:
                return False

            if len(word) == 1 and word == board[row][col]:
                return True

            if curr_idx == len(word)-1 and curr_idx>0:
                return True

            res = False
            for direction in directions:
                row_ = row + direction[0]
                col_ = col + direction[1]
                
                if (row_, col_) not in visited and 0 <= row_ <= len(board)-1 and 0 <= col_ <= len(board[0])-1:
                    
                    if curr_idx+1<len(word) and board[row_][col_] == word[curr_idx+1]:
                        isExists = True
                        res = res or dfs(row_, col_, curr_idx+1, visited+[(row, col)])
            
            if not isExists: return False
            return res

        ret = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                ret = ret or dfs(row, col, 0, [])
        return ret
    

    def exist(self, board: List[List[str]], word: str) -> bool: 

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(row, col, index):
            
            if index == 0:
                if len(word) == 1 and word[index] == board[row][col]:
                    return True
            else:
                if index == len(word)-1:
                    return True

            visited[row][col] = True

            for dr, dc in directions:
                if (
                0 <= row+dr <= rows-1 and 0 <= col+dc <= cols-1 
                and index+1 <= len(word)-1
                and not visited[row+dr][col+dc] 
                and word[index+1] == board[row+dr][col+dc]):
                    if dfs(row+dr, col+dc, index+1):
                        return True
                    
            visited[row][col] = False
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


cases = [
    ([["A"]], "A", True),
    ([["A", "B", "C"], ["D", "E", "F"]], "FEDABC", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ASA", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A", "A", "A"], ["B", "B", "B"]], "C", False),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ([["A", "B"]], "BA", True),
]

@pytest.mark.parametrize(
    "bord, word, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases)+1)]

)
def test_case(bord, word, expected):
    actual = Solution().exist(bord, word)
    assert actual == expected