#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # 左側から英数字まで移動
            while left < right and not s[left].isalnum():
                left += 1
            # 右側から英数字まで移動
            while left < right and not s[right].isalnum():
                right -= 1

            # 小文字にして比較する
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
        
# @lc code=end

