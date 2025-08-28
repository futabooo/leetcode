#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is not None:
            # 左側の子ノードを再帰的に訪問
            self._inorder_helper(node.left, result)
            # 自分の値を記録
            result.append(node.val)
            # 右側の子ノードを再帰的に訪問
            self._inorder_helper(node.right, result)


# @lc code=end
