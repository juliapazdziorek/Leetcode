# 11. Container With Most Water (Medium)

**Topics:** two pointers, greedy  
**Time:** O(n) · **Space:** O(1)

## Idea
Pointers at both ends. Area = `min(h[l], h[r]) * (r - l)`. Always move the pointer at the *shorter* line — the shorter line limits the area, and moving the taller one can only make the width smaller without raising the height limit.

## Pitfalls
- Moving the taller side never helps — that's the key greedy argument.
