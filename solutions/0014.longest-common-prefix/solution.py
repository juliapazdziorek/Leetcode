# Created by Jula at 2026/08/06 13:13
# leetgo: 1.4.17
# https://leetcode.com/problems/longest-common-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        str_first = strs[0]
        str_last = strs[-1]
        result = ''

        for i in range(min(len(str_first), len(str_last))):
            if str_first[i] == str_last[i]:
                result += str_first[i]
            else:
                break

        return result

        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestCommonPrefix(strs)
    print("\noutput:", serialize(ans, "string"))
