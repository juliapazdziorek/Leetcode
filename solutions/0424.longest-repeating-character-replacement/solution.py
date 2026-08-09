# Created by Jula at 2026/08/09 18:40
# leetgo: 1.4.17
# https://leetcode.com/problems/longest-repeating-character-replacement/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        window_dict = {}
        window_len = 0

        for right in range(len(s)):
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1
            window_len += 1

            if window_len - max(window_dict.values()) > k:
                window_dict[s[left]] -= 1
                window_len -= 1
                left += 1

            result = max(result, window_len)

        return result




        # @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().characterReplacement(s, k)
    print("\noutput:", serialize(ans, "integer"))
