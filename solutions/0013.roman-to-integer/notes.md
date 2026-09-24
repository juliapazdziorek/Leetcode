# 13. Roman to Integer (Easy)

**Topics:** hash map, string  
**Time:** O(n) · **Space:** O(1)

## Idea
Map symbols to values. Walk the string from the right: if the current symbol is smaller than the one to its right (e.g. `I` before `V`), subtract it, otherwise add it.

## Pitfalls
- Subtractive cases: IV, IX, XL, XC, CD, CM.
