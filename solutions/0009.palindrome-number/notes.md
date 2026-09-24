# 9. Palindrome Number (Easy)

**Topics:** math  
**Time:** O(log x) · **Space:** O(1)

## Idea
Negative numbers are never palindromes. Get the number of digits with `log10`, then repeatedly compare the first digit (`x // 10**(len-1)`) with the last (`x % 10`), strip both and shrink the length by 2.

## Pitfalls
- `log10(0)` is undefined — handle 0 separately.

## Alternative
Reverse only the second half of the number and compare with the first half. Or simply `str(x) == str(x)[::-1]`.
