# 167. Two Sum II - Input Array Is Sorted (Medium)

**Topics:** two pointers  
**Time:** O(n) · **Space:** O(1)

## Idea
Array is sorted. Pointers at both ends: sum too small → `l += 1`, too big → `r -= 1`, until the sum equals target.

## Pitfalls
- Answer is 1-indexed.
