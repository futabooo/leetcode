#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for i, x in enumerate(nums):
            if x in last_index and i - last_index[x] <= k:
                return True
            last_index[x] = i
        return False


# @lc code=end
