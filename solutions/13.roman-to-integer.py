#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for roman in s:
            value = roman_int_map[roman]
            # 現在の値が前の値より大きい場合、前の値は1度足してしまっているのでその分と、ルールにある小さい値を引くを適用する
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
            
        return total
        
# @lc code=end

