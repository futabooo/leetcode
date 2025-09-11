#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # XOR演算を使用して、2回現れる数を消す
            result ^= num
        return result


# @lc code=end
