from typing import Optional, List
from collections import deque
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0

        def dfs(root: TreeNode) -> int:

            nonlocal count, res

            if root.left is not None:
                dfs(root.left)

            count += 1
            if count == k:
                res = root.val

            if root.right is not None:
                dfs(root.right)

        dfs(root)
        return res


def build_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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
    ([3, 1, 4, None, 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ([1], 1, 1),
]


@pytest.mark.parametrize(
    "root_list, k, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(root_list, k, expected):
    root = build_binary_tree(root_list)
    actual = Solution().kthSmallest(root, k)
    assert actual == expected
