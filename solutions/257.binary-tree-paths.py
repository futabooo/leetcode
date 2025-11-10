#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        paths = []

        def construct_paths(node: Optional[TreeNode], path: str) -> None:
            if node:
                path += str(node.val)
                if node.left is None and node.right is None:
                    paths.append(path)
                else:
                    path += "->"
                    construct_paths(node.left, path)
                    construct_paths(node.right, path)

        construct_paths(root, "")
        return paths


# @lc code=end
