# Created by Jula at 2026/07/23 12:14
# leetgo: 1.4.17
# https://leetcode.com/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[nums[i]] = i

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
