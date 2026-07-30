# Created by Jula at 2026/07/30 11:58
# leetgo: 1.4.17
# https://leetcode.com/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        parentheses_map = {')':'(', ']': '[','}': '{' }

        for char in s:
            if char in parentheses_map:
                if not stack or stack.pop() != parentheses_map[char]:
                    return False
            else:
                stack.append(char)

        if stack:
            return False

        return True

        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
