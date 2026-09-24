# 1. Two Sum (Easy)

**Topics:** hash map  
**Time:** O(n) · **Space:** O(n)

## Idea
One pass. For each number compute `diff = target - num`. If `diff` was already seen, return its stored index and the current one; otherwise store `num -> index` in the map.

## Pitfalls
- Check the map *before* inserting the current number, so an element is never paired with itself.
