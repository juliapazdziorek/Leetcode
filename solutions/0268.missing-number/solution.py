# Created by Jula at 2026/07/24 13:44
# leetgo: 1.4.17
# https://leetcode.com/problems/missing-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().missingNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
