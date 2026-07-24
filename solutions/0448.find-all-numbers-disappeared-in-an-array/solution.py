# Created by Jula at 2026/07/24 14:04
# leetgo: 1.4.17
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                result.append(i)

        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDisappearedNumbers(nums)
    print("\noutput:", serialize(ans, "integer[]"))
