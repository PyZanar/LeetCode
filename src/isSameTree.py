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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # True確定
        if not p and not q:
            return True
        # False確定
        elif (not p and q) or (p and not q) or (p.val != q.val):
            return False

        # 左右の部分木を走査
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([None], [None], True),
    ([1, 2, 1], [1, 1, 2], False),
]


@pytest.mark.parametrize(
    "p, q, expected", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(p, q, expected):
    p_root = build_binary_tree(p)
    q_root = build_binary_tree(q)
    actual = Solution().isSameTree(p_root, q_root)
    assert actual == expected
