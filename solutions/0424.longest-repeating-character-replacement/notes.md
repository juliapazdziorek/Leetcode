# 424. Longest Repeating Character Replacement (Medium)

**Topics:** sliding window, hash map  
**Time:** O(n · 26) = O(n) · **Space:** O(26) = O(1)

## Idea
Window is valid if `window_len - count_of_most_frequent_char <= k` (the rest can be replaced). Extend `right`; if the window becomes invalid, move `left` by **one** (the window slides, never shrinks). The answer is the largest window size reached.

## Pitfalls
- Using `if` instead of `while` is intentional — a smaller window can't beat the best one, so we just slide it.

## Alternative
Keep `max_freq` as a variable (never decreasing) instead of `max(dict.values())` → true O(n).
