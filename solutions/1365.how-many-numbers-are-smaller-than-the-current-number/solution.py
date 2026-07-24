# Created by Jula at 2026/07/24 14:38
# leetgo: 1.4.17
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        nums_dict = {}

        for i, num in enumerate(nums_sorted):
            if num not in nums_dict:
                nums_dict[num] = i

        result = []
        for num in nums:
            result.append(nums_dict[num])

        return result

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallerNumbersThanCurrent(nums)
    print("\noutput:", serialize(ans, "integer[]"))
