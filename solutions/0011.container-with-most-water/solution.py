# Created by Jula at 2026/07/29 21:06
# leetgo: 1.4.17
# https://leetcode.com/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        l = 0
        r = len(height) - 1
        while l < r:
            result = max(result, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result
        

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)
    print("\noutput:", serialize(ans, "integer"))
