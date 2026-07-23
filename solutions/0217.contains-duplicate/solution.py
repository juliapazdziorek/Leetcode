# Created by Jula at 2026/07/23 12:46
# leetgo: 1.4.17
# https://leetcode.com/problems/contains-duplicate/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        return False

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().containsDuplicate(nums)
    print("\noutput:", serialize(ans, "boolean"))
