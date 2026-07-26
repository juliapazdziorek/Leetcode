# Created by Jula at 2026/07/26 17:07
# leetgo: 1.4.17
# https://leetcode.com/problems/maximum-product-of-three-numbers/
from cmath import inf
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_one, max_two, max_three = -inf, -inf, -inf
        min_one, min_two = inf, inf

        for num in nums:
            if num >= max_one:
                max_three = max_two
                max_two = max_one
                max_one = num
            elif num >= max_two:
                max_three = max_two
                max_two = num
            elif num > max_three:
                max_three = num

            if num <= min_one:
                min_two = min_one
                min_one = num
            elif num < min_two:
                min_two = num

        return max(max_one * max_two * max_three, max_one * min_one * min_two)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
