# 238. Product of Array Except Self (Medium)

**Topics:** prefix sum (prefix product), array  
**Time:** O(n) · **Space:** O(1) extra (output array not counted)

## Idea
`answer[i]` = product of everything left of `i` × product of everything right of `i`. First pass left→right writes the prefix product into `result`; second pass right→left multiplies it by a running suffix product.

## Pitfalls
- No division allowed (and zeros would break it anyway).
