# Created by Jula at 2026/07/27 17:45
# leetgo: 1.4.17
# https://leetcode.com/problems/valid-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [char for char in s.lower() if 'a' <= char <= 'z' or '0' <= char <= '9']

        l = 0
        r = len(char_list) - 1

        while l < r:
            if char_list[l] != char_list[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

        # result = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # return result == result[::-1]
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isPalindrome(s)
    print("\noutput:", serialize(ans, "boolean"))
