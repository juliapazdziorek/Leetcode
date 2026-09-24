# 628. Maximum Product of Three Numbers (Easy)

**Topics:** array, math  
**Time:** O(n) · **Space:** O(1)

## Idea
The max product is either the three largest numbers, or the largest number times the two smallest (two negatives make a positive). Track the top 3 maxima and the bottom 2 minima in one pass.

## Pitfalls
- Negative numbers! `max1 * min1 * min2` can beat `max1 * max2 * max3`.

## Alternative
Sort and compare `nums[-1]*nums[-2]*nums[-3]` with `nums[0]*nums[1]*nums[-1]` → O(n log n).
