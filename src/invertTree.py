from typing import Optional, List
from collections import deque
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    # True確定
    if not p and not q:
        return True
    # False確定
    elif (not p and q) or (p and not q) or (p.val != q.val):
        return False

    # 左右の部分木を走査
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)

        return root


cases = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
]


@pytest.mark.parametrize(
    "root_list, expected_list",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases) + 1)],
)
def test_case(root_list, expected_list):
    root = build_binary_tree(root_list)
    actual = Solution().invertTree(root)
    expected = build_binary_tree(expected_list)
    assert isSameTree(actual, expected)
