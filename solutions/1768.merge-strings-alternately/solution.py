# Created by Jula at 2026/07/23 12:14
# leetgo: 1.4.17
# https://leetcode.com/problems/merge-strings-alternately/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0
        new_word = []

        while i1 < len(word1) and i2 < len(word2):
            new_word.append(word1[i1])
            i1 += 1

            new_word.append(word2[i2])
            i2 += 1

        new_word.append(word1[i1:])
        new_word.append(word2[i2:])

        return "".join(new_word)

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().mergeAlternately(word1, word2)
    print("\noutput:", serialize(ans, "string"))
