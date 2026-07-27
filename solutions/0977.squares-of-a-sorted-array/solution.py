# Created by Jula at 2026/07/27 17:34
# leetgo: 1.4.17
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        result = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1

        result.reverse()
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedSquares(nums)
    print("\noutput:", serialize(ans, "integer[]"))
