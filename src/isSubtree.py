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


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # True確定
            if not root and not subRoot:
                return True
            # False確定
            elif (
                (not root and subRoot)
                or (root and not subRoot)
                or (root.val != subRoot.val)
            ):
                return False

            # 左右の部分木を走査
            return isSametree(root.left, subRoot.left) and isSametree(
                root.right, subRoot.right
            )

        def helper(root: Optional[TreeNode]) -> bool:

            if not root:
                return False

            if root.val == subRoot.val:
                if isSametree(root, subRoot):
                    return True

            return helper(root.left) or helper(root.right)

        return helper(root)


cases = [
    ([3, 4, 5, 1, 2], [4, 1, 2], True),
    ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ([1, 1], [1], True),
]


@pytest.mark.parametrize(
    "root_list, subRoot_list, expected",
    cases,
    ids=[f"case_{i}" for i in range(1, len(cases) + 1)],
)
def test_case(root_list, subRoot_list, expected):
    root = build_binary_tree(root_list)
    subRoot = build_binary_tree(subRoot_list)
    actual = Solution().isSubtree(root, subRoot)
    assert actual == expected
