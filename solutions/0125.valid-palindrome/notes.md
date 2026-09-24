# 125. Valid Palindrome (Easy)

**Topics:** two pointers, string  
**Time:** O(n) · **Space:** O(n)

## Idea
Lowercase and keep only alphanumeric characters, then compare from both ends with two pointers moving inward.

## Alternative
Skip non-alphanumeric chars on the fly with the pointers on the original string → O(1) extra space.
