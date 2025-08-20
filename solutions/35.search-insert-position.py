#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        insert_index = 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i

            if nums[i] < target:
                insert_index = i + 1

        return insert_index


# @lc code=end
