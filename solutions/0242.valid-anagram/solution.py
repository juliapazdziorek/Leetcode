# Created by Jula at 2026/07/23 13:01
# leetgo: 1.4.17
# https://leetcode.com/problems/valid-anagram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1

        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1

        return s_dict == t_dict
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isAnagram(s, t)
    print("\noutput:", serialize(ans, "boolean"))
