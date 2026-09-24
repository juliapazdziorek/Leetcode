# 1464. Maximum Product of Two Elements in an Array (Easy)

**Topics:** array, greedy  
**Time:** O(n) · **Space:** O(1)

## Idea
The answer is `(max1 - 1) * (max2 - 1)`, so just find the two largest numbers in one pass.

## Pitfalls
- Use `>=` for the first max, so duplicates of the maximum fill the second slot too.
