#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self._is_mirror(root.left, root.right)

    def _is_mirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        # 鏡なので左の左と右の右、左の右と右の左を比較していく
        return (
            left.val == right.val
            and self._is_mirror(left.left, right.right)
            and self._is_mirror(left.right, right.left)
        )


# @lc code=end
