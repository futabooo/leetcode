#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # min,maxを使うと与えられた文字列の配列を辞書順でソートした上で
        # 最初と最後を比較する、このとき同じ文字は間の文字列でも同じになる
        min_str = min(strs)
        max_str = max(strs)
        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str
