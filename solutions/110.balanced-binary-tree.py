#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_height = self._getHeight(root.left)
        right_height = self._getHeight(root.right)

        return (
            abs(left_height - right_height) <= 1
            and left_height != -1
            and right_height != -1
        )

    def _getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self._getHeight(root.left)
        right_height = self._getHeight(root.right)

        if (
            left_height == -1
            or right_height == -1
            or abs(left_height - right_height) > 1
        ):
            return -1
        return max(left_height, right_height) + 1


# @lc code=end
