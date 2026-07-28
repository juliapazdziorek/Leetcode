# Created by Jula at 2026/07/28 20:07
# leetgo: 1.4.17
# https://leetcode.com/problems/longest-mountain-in-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        size = len(arr)
        result = 0

        for i in range(1, size - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = i
                r = i

                while l - 1 >= 0 and arr[l - 1] < arr[l]:
                    l -= 1
                while r + 1 < size and arr[r] > arr[r + 1]:
                    r += 1

                result = max(result, r - l + 1)

        return result


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestMountain(arr)
    print("\noutput:", serialize(ans, "integer"))
