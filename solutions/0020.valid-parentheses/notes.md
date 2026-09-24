# 20. Valid Parentheses (Easy)

**Topics:** stack, hash map  
**Time:** O(n) · **Space:** O(n)

## Idea
Push opening brackets on a stack. For a closing bracket, the top of the stack must be its matching opening bracket (map closing → opening); otherwise invalid. At the end the stack must be empty.

## Pitfalls
- Closing bracket with an empty stack → invalid.
- Leftover opening brackets → invalid.
