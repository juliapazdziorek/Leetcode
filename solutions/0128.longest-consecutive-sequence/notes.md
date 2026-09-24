# 128. Longest Consecutive Sequence (Medium)

**Topics:** hash set  
**Time:** O(n) · **Space:** O(n)

## Idea
Put all numbers in a set. A number starts a sequence only if `num - 1` is **not** in the set. From each start, count upwards while `num + 1` exists. Each number is visited at most twice → O(n).

## Pitfalls
- Iterate over the set, not the list, to avoid re-counting duplicates.
- Without the `num - 1` check it becomes O(n²).
