# Created by Jula at 2026/08/06 13:47
# leetgo: 1.4.17
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        last = 0
        result_nums = []

        while last < len(nums) - 1:
            if nums[first] == nums[last]:
                last += 1
            else:
                result_nums.append(nums[first])
                first = last
                last += 1

        length_nums = len(nums)
        nums = result_nums
        return length_nums - len(result_nums)

        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().removeDuplicates(nums)
    print("\noutput:", serialize(ans, "integer"))
   