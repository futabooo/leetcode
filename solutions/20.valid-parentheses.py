#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            # 閉じ括弧ならスタックのトップと比較
            if char in parentheses_map:
                # 対応する開き括弧をスタックから取り出す
                top_element = stack.pop() if stack else "#"
                if parentheses_map[char] != top_element:
                    # 対応する開き括弧がスタックのトップにない場合はFalse
                    return False
            # 開き括弧ならスタックに追加
            else:
                stack.append(char)

        return not stack


# @lc code=end
