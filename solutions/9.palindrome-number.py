#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # マイナスは回文ではない
        if x < 0:
            return False

        # 文字列にして逆順と比較する
        str_x = str(x)
        return str_x == str_x[::-1]
# @lc code=end

