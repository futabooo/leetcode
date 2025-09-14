#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorderHelper(root, result)
        return result

    def postorderHelper(self, node, result):
        if not node:
            return
        self.postorderHelper(node.left, result)
        self.postorderHelper(node.right, result)
        result.append(node.val)


# @lc code=end
