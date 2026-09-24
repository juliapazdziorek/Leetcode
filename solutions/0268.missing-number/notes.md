# 268. Missing Number (Easy)

**Topics:** math  
**Time:** O(n) · **Space:** O(1)

## Idea
The numbers are `0..n` with one missing. Expected sum `n(n+1)/2` minus the actual sum = the missing number.

## Alternative
XOR all indices `0..n` with all values — pairs cancel out, the missing number remains.
