# 1768. Merge Strings Alternately (Easy)

**Topics:** two pointers, string  
**Time:** O(n + m) · **Space:** O(n + m)

## Idea
One index per word; while both have characters, append one from each alternately. Then append the leftover tail of the longer word (`word[i:]`). Build a list and `''.join()` it.

## Pitfalls
- String `+=` in a loop is O(n²) in the worst case — collect into a list.
