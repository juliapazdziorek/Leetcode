# Created by Jula at 2026/07/27 16:40
# leetgo: 1.4.17
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = 0
        sec_max = 0

        for num in nums:
            if num >= first_max:
                sec_max = first_max
                first_max = num
            elif num > sec_max:
                sec_max = num

        return (first_max - 1) * (sec_max - 1)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
