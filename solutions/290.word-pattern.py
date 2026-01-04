#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # 長さが異なる場合はパターンに一致しない
        if len(pattern) != len(words):
            return False

        # 双方向のマッピングを保存する辞書を作成
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            # charが既に別のwordにマッピングされている
            if char in char_to_word and char_to_word[char] != word:
                return False
            # wordが既に別のcharにマッピングされている
            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True


# @lc code=end
