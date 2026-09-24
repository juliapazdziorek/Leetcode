# 3. Longest Substring Without Repeating Characters (Medium)

**Topics:** sliding window, hash set  
**Time:** O(n) · **Space:** O(min(n, alphabet))

## Idea
Window `[left, right]` with a set of its characters. Extend `right`; while `s[right]` is already in the set, remove `s[left]` and move `left` forward. After each step the window has no repeats, so update the answer with its length `right - left + 1`.

## Pitfalls
- Substring (contiguous) ≠ subsequence.

## Alternative
Store `char -> last index` in a map and jump `left` directly past the previous occurrence.
