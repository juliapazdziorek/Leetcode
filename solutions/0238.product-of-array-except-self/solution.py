# Created by Jula at 2026/07/23 16:04
# leetgo: 1.4.17
# https://leetcode.com/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        left = 1
        right = 1

        for i in range(size):
            result[i] = left
            left *= nums[i]

        for i in range(size - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result

        # @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)
    print("\noutput:", serialize(ans, "integer[]"))
