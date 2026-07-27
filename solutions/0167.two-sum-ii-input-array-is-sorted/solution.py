# Created by Jula at 2026/07/27 18:14
# leetgo: 1.4.17
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        sum_lr = numbers[l] + numbers[r]

        while sum_lr != target:
            if sum_lr < target:
                l += 1
            elif sum_lr > target:
                r -= 1

            sum_lr = numbers[l] + numbers[r]

        return [l + 1, r + 1]
        

# @lc code=end

if __name__ == "__main__":
    numbers: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(numbers, target)
    print("\noutput:", serialize(ans, "integer[]"))
