# Created by Jula at 2026/07/26 12:05
# leetgo: 1.4.17
# https://leetcode.com/problems/number-of-islands/
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        visited = set()
        stack = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        col_len = len(grid)
        row_len = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if (i,j) in visited:
                    continue

                if grid[i][j] == '0':
                    continue

                islands += 1
                stack.append((i, j))

                while stack:
                    cur_i, cur_j = stack.pop()
                    visited.add((cur_i, cur_j))

                    for direction in directions:
                        new_i, new_j = cur_i + direction[0], cur_j + direction[1]
                        if 0 <= new_i < col_len and 0 <= new_j < row_len and grid[new_i][new_j] == '1' and (new_i, new_j) not in visited:
                            stack.append((new_i, new_j))

        return islands

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numIslands(grid)
    print("\noutput:", serialize(ans, "integer"))
