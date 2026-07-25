# Created by Jula at 2026/07/25 13:28
# leetgo: 1.4.17
# https://leetcode.com/problems/minimum-time-visiting-all-points/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        start_x, start_y = points[0]
        for point in points[1:]:
            end_x, end_y = point
            distance_x = abs(start_x - end_x)
            distance_y = abs(start_y - end_y)
            time += max(distance_x, distance_y)
            start_x, start_y = end_x, end_y
        return time


        # @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTimeToVisitAllPoints(points)
    print("\noutput:", serialize(ans, "integer"))
