# Created by Jula at 2026/08/06 12:11
# leetgo: 1.4.17
# https://leetcode.com/problems/roman-to-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s) - 1, -1, -1):
            if i + 1 <= len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]

        return result
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().romanToInt(s)
    print("\noutput:", serialize(ans, "integer"))
