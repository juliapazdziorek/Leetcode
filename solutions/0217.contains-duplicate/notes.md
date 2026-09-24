# 217. Contains Duplicate (Easy)

**Topics:** hash set  
**Time:** O(n) · **Space:** O(n)

## Idea
Build a set from the list; if it's shorter than the list, some element was repeated.

## Alternative
Loop and return early at the first element already in the set.
