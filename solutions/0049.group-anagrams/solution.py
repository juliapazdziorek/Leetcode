# Created by Jula at 2026/07/23 13:08
# leetgo: 1.4.17
# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups[tuple(sorted(word))].append(word)

        return list(groups.values())

        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
