# 49. Group Anagrams (Medium)

**Topics:** hash map, sorting, string  
**Time:** O(n · k log k) · **Space:** O(n · k)

## Idea
Anagrams become identical after sorting their letters. Use `tuple(sorted(word))` as the key in a `defaultdict(list)` and group words under it.

## Pitfalls
- Lists aren't hashable — use a tuple (or string) as the key.

## Alternative
Key = tuple of 26 letter counts → O(n · k).
