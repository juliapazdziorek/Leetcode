# 448. Find All Numbers Disappeared in an Array (Easy)

**Topics:** hash set, array  
**Time:** O(n) · **Space:** O(n)

## Idea
Put all numbers in a set, then check every value `1..n` and collect those not in the set.

## Alternative
O(1) extra space: for each value `v`, mark index `|v| - 1` negative; indices still positive are the missing numbers.
