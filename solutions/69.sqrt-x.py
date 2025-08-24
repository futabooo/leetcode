#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        # 二分探索、2以上の平方根はx//2以下になるため最大値をx//2に設定
        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


# @lc code=end
