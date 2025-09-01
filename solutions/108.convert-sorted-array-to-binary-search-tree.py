#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # 照準に並んでいるので真ん中を根にして左右に分割を繰り返していく
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # 左半分で再起的に木を作る
        root.left = self.sortedArrayToBST(nums[:mid])

        # 右半分で再起的に木を作る
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root


# @lc code=end
