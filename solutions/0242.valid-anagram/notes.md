# 242. Valid Anagram (Easy)

**Topics:** hash map, counting  
**Time:** O(n) · **Space:** O(1) (at most 26 keys)

## Idea
If lengths differ → not an anagram. Otherwise count characters of both strings in two dicts and compare them.

## Alternative
`Counter(s) == Counter(t)`, or `sorted(s) == sorted(t)` in O(n log n).
