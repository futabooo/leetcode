#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_depth(node: Optional[TreeNode]) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def right_depth(node: Optional[TreeNode]) -> int:
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        lh = left_depth(root)
        rh = right_depth(root)
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# @lc code=end
