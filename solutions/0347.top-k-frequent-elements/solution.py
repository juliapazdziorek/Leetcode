# Created by Jula at 2026/07/23 14:21
# leetgo: 1.4.17
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # counter = Counter(nums)
        # items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # return [number for number, frequency in items[:k]]

        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in nums_dict.items():
            buckets[value].append(key)

        result = []
        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result

        return result



# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
