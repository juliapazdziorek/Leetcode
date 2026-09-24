# 36. Valid Sudoku (Medium)

**Topics:** hash set, matrix  
**Time:** O(81) = O(1) · **Space:** O(81) = O(1)

## Idea
One set per row, per column and per 3×3 box. For each filled cell check whether its digit is already in its row/column/box set; if yes → invalid, otherwise add it to all three.

## Pitfalls
- Box index: `(i // 3) * 3 + j // 3`.
