# Created by Jula at 2026/07/25 13:09
# leetgo: 1.4.17
# https://leetcode.com/problems/maximum-product-of-two-digits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        second_largest = 0
        while n > 0:
            num = n % 10
            if num >= largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
            n //= 10
        return largest * second_largest

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().maxProduct(n)
    print("\noutput:", serialize(ans, "integer"))
