#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            # 1引くことで0ベースに調整
            columnNumber -= 1
            # 26で割った余りを計算
            remainder = columnNumber % 26
            # 余りを文字に変換して結果に追加
            result.append(chr(remainder + ord("A")))
            # 26で割って次の桁へ
            columnNumber //= 26
        return "".join(reversed(result))


# @lc code=end
