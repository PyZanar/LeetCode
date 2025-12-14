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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(root: Optional[TreeNode]) -> List[int]:

            nonlocal res

            if not root:
                res = []
                return

            res.append(root.val)

            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

        dfs(root)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []
        stack: List[TreeNode] = []
        curr: TreeNode = root

        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            curr = stack.pop()

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
    ([1, None, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [1, 2, 4, 5, 6, 7, 3, 8, 9]),
    ([], []),
    ([1], [1]),
]


@pytest.mark.parametrize(
    "root_list, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(root_list, expected):
    root = build_binary_tree(root_list)
    actual = Solution().preorderTraversal2(root)
    assert actual == expected
