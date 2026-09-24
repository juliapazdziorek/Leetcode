# 3536. Maximum Product of Two Digits (Easy)

**Topics:** math, greedy  
**Time:** O(d) (number of digits) · **Space:** O(1)

## Idea
Extract digits with `n % 10` / `n //= 10` and keep the two largest ones; the answer is their product.

## Pitfalls
- Same digit may appear twice (e.g. 99 → 81) — `>=` handles it.
