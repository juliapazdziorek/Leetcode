# Created by Jula at 2026/07/23 19:28
# leetgo: 1.4.17
# https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = 9
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(board_size):
            for j in range(board_size):

                num = board[i][j]

                if num == '.':
                    continue

                box = i // 3 * 3 + j // 3

                if num in row_sets[i] or num in col_sets[j] or num in box_sets[box]:
                    return False

                row_sets[i].add(num)
                col_sets[j].add(num)
                box_sets[box].add(num)

        return True


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().isValidSudoku(board)
    print("\noutput:", serialize(ans, "boolean"))
