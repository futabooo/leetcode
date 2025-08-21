#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        # 文字列を空白で分割する
        words = s.split()

        # 最後の単語の長さを返す
        return len(words[-1]) if words else 0


# @lc code=end
