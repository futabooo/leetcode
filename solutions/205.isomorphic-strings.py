#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            else:
                s_to_t[cs] = ct

            if ct in t_to_s:
                if t_to_s[ct] != cs:
                    return False
            else:
                t_to_s[ct] = cs

        return True

# @lc code=end

