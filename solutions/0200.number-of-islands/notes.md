# 200. Number of Islands (Medium)

**Topics:** graph, DFS, matrix  
**Time:** O(m · n) · **Space:** O(m · n)

## Idea
Scan the grid. Every unvisited `'1'` starts a new island: increment the counter and flood-fill (iterative DFS with a stack) over its 4-directional land neighbours, marking them visited.

## Pitfalls
- Check bounds before accessing neighbours.

## Alternative
Mark visited land by overwriting it with `'0'` instead of keeping a `visited` set.
