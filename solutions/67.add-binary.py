#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 10進数にする
        number_a = int(a, 2)
        number_b = int(b, 2)

        # 足したあと2進数に戻す、先頭の'0b'を削る
        return bin(number_a + number_b)[2:]


# @lc code=end
