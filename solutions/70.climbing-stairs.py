#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 最初の2段
        if n <= 2:
            return n

        # 3段目以降は前の2段の和となる
        first, second = 1, 2
        for _ in range(3, n + 1):
            # 1段増えたらその前の2段を更新
            first, second = second, first + second

        return second


# @lc code=end
