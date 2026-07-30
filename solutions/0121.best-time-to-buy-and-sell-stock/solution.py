# Created by Jula at 2026/07/30 12:54
# leetgo: 1.4.17
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from cmath import inf
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        result = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > result:
                result = prices[i] - min_price

        return result

# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
