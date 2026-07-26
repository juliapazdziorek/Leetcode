# Created by Jula at 2026/07/26 17:42
# leetgo: 1.4.17
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                cur_num = num

                while cur_num + 1 in nums_set:
                    length += 1
                    cur_num += 1

                result = max(result, length)

        return result

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestConsecutive(nums)
    print("\noutput:", serialize(ans, "integer"))
