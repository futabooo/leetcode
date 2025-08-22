#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        # 配列の末尾から順にループさせる
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # 9の繰り上がりで0にして次の桁に進む
            digits[i] = 0

        # すべての桁が9だった場合、新しい桁を追加
        return [1] + digits
