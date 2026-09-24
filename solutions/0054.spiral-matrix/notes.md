# 54. Spiral Matrix (Medium)

**Topics:** matrix, simulation  
**Time:** O(m · n) · **Space:** O(1) extra

## Idea
Keep four boundaries: top, bottom, left, right. Walk right along top row → top++, down the right column → right--, left along bottom row → bottom--, up the left column → left++. Repeat until all `m·n` elements are collected.

## Pitfalls
- Check whether everything was collected after each direction — otherwise non-square matrices get duplicates.
