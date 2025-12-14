from typing import List, Optional
from collections import deque
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        a = 3

        def dfs(root: Optional[TreeNode]) -> List[int]:

            nonlocal res

            if not root:
                res = []
                return

            if root.left:
                dfs(root.left)

            res.append(root.val)

            if root.right:
                dfs(root.right)

        dfs(root)
        return res

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:

        res: List[int] = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


def build_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:

    if not values:
        return None

    idx = 0
    que = deque([])
    root = TreeNode(values[idx])
    que.append(root)

    while que:
        curr: TreeNode = que.popleft()

        idx += 1
        if idx >= len(values):
            break
        if values[idx] is not None:
            curr.left = TreeNode(values[idx])
            que.append(curr.left)

        idx += 1
        if idx >= len(values):
            break
        if values[idx] is not None:
            curr.right = TreeNode(values[idx])
            que.append(curr.right)

    return root


cases = [
    ([1, None, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
    ([], []),
    ([1], [1]),
]


@pytest.mark.parametrize(
    "root_list, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(root_list, expected):
    root = build_binary_tree(root_list)
    actual = Solution().inorderTraversal2(root)
    assert actual == expected
