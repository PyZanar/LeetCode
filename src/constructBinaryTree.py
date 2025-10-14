from typing import List, Optional
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: Optional[List[int]], inorder: Optional[List[int]]) -> Optional[TreeNode]: 
        # 値→位置のマップを作る
        idx_map = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0  # ここを進めながら根を決める

        def helper(in_left, in_right):
            nonlocal preorder_index
            # 終了条件
            if in_left > in_right:
                return None

            # 1. preorder から根を取り出す
            root_val = preorder[preorder_index]
            preorder_index += 1

            # 2. ノードを作る
            root = TreeNode(root_val)

            # 3. inorder の位置で分けて左右を作る
            index = idx_map[root_val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)


class Solution2:
    def buildTree(self, preorder: Optional[List[int]], inorder: Optional[List[int]]) -> Optional[TreeNode]: 
        
        if not preorder:
            return None
        
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        idx = idx_map[root_val]
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

        

    

def preorder_traversal(root):
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


@pytest.mark.parametrize(
    "preorder, inorder",
    [
        ([3,9,20,15,7], [9,3,15,20,7]),
        ([1,2,3], [2,1,3]),
        ([1], [1]),
    ]
)
def test_build_tree(preorder, inorder):
    sol = Solution2()
    root = sol.buildTree(preorder, inorder)
    assert preorder_traversal(root) == preorder
    assert inorder_traversal(root) == inorder
        

