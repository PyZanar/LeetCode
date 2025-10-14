from typing import List
import pytest

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(curr_str: str, open_remaining: int, close_remaining: int):

            # 終了条件
            if open_remaining == 0 and close_remaining == 0:
                res.append(curr_str)
                return
            
            # '(' を追加可能なら追加
            if open_remaining > 0:
                dfs(curr_str+"(", open_remaining-1, close_remaining)

            # ')' を追加可能なら追加
            if close_remaining > open_remaining:
                dfs(curr_str+")", open_remaining, close_remaining-1)

        dfs("", n, n)
        return res
            
sol =Solution()
actual = print(sorted(sol.generateParenthesis(3)))

@pytest.mark.parametrize(
    "n, expected",
    [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"])
    ]
)
def test_case(n, expected):
    sol =Solution()
    actual = sorted(sol.generateParenthesis(n))
    expected = sorted(expected)
    assert actual == expected