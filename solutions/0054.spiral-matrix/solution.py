# Created by Jula at 2026/07/25 19:59
# leetgo: 1.4.17
# https://leetcode.com/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col_len = len(matrix)
        row_len = len(matrix[0])

        i, j = 0, 0

        result = []
        res_len = row_len * col_len
        res_counter = 0

        right_bound = row_len - 1
        down_bound = col_len - 1
        left_bound = 0
        up_bound = 0

        while res_counter < res_len:

            for j in range(left_bound, right_bound + 1):
                result.append(matrix[i][j])
                res_counter += 1
            up_bound += 1

            if res_counter == res_len:
                break

            for i in range(up_bound, down_bound + 1):
                result.append(matrix[i][j])
                res_counter += 1
            right_bound -= 1

            if res_counter == res_len:
                break

            for j in range(right_bound, left_bound - 1, - 1):
                result.append(matrix[i][j])
                res_counter += 1
            down_bound -= 1

            if res_counter == res_len:
                break

            for i in range(down_bound, up_bound - 1, - 1):
                result.append(matrix[i][j])
                res_counter += 1
            left_bound += 1

        return result

    # @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
