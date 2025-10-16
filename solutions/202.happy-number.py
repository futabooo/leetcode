#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares(number: int) -> int:
            total = 0
            while number > 0:
                digit = number % 10
                total += digit**2
                number //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_sum_of_squares(n)
        return n == 1


# @lc code=end
