#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # 最下位ビットを取得
            bit = n & 1
            # resultを左シフトして新しいビットを追加
            result = (result << 1) | bit
            # nを右シフト
            n >>= 1
        return result


# @lc code=end
