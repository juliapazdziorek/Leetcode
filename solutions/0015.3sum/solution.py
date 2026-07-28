# Created by Jula at 2026/07/27 22:51
# leetgo: 1.4.17
# https://leetcode.com/problems/3sum/
from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        size = len(nums)
        last_i = size - 1
        nums.sort()

        for i in range(size - 2):
            if i - 1 >= 0 and nums[i] ==  nums[i - 1]:
                continue

            l = i + 1
            r = last_i
            sum_lr = nums[l] + nums[r]

            while l < r:
                if sum_lr < -nums[i]:
                    l += 1
                elif sum_lr > -nums[i]:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l - 1 < size - 1 and l < size - 1 and nums[l] == nums[l - 1]:
                        l += 1

                sum_lr = nums[l] + nums[r]

        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeSum(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
