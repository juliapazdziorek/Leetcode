# 15. 3Sum (Medium)

**Topics:** two pointers, sorting  
**Time:** O(n²) · **Space:** O(1) extra (ignoring output / sort)

## Idea
Sort. Fix `nums[i]` and look for a pair in `nums[i+1:]` summing to `-nums[i]` with two pointers (Two Sum II). Too small → `l += 1`, too big → `r -= 1`, match → record it and move both.

## Pitfalls
- Skip duplicate values of `nums[i]` (compare with `nums[i-1]`).
- After a match, skip duplicate `nums[l]` values too, or you'll output the same triplet twice.
