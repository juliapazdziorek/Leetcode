# 1266. Minimum Time Visiting All Points (Easy)

**Topics:** math, geometry  
**Time:** O(n) · **Space:** O(1)

## Idea
Moving diagonally covers 1 unit in both x and y in one second, so the time between two points is `max(|dx|, |dy|)` (Chebyshev distance). Sum it over consecutive pairs.
