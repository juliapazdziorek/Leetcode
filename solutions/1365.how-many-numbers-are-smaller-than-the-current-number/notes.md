# 1365. How Many Numbers Are Smaller Than the Current Number (Easy)

**Topics:** sorting, hash map  
**Time:** O(n log n) · **Space:** O(n)

## Idea
In the sorted array, the index of the **first** occurrence of a value equals how many numbers are smaller than it. Store `value -> first index` in a dict, then map the original array through it.

## Pitfalls
- Only store the first index — duplicates must not overwrite it.

## Alternative
Values are in 0..100 → counting sort + prefix sums in O(n + 100).
