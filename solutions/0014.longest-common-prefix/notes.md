# 14. Longest Common Prefix (Easy)

**Topics:** string, sorting  
**Time:** O(n · m · log n) · **Space:** O(1) extra

## Idea
Sort the strings lexicographically. The first and last strings are the most different ones, so the common prefix of *just those two* is the common prefix of all of them. Compare them char by char.

## Alternative
Vertical scan: compare character `i` across all strings, stop at first mismatch — O(total chars) without sorting.
