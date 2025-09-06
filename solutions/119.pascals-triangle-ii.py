#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        # 全部1で行数と同じ長さのリストを作成
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            # 後ろから更新していく
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row


# @lc code=end
