# 977. Squares of a Sorted Array (Easy)

**Topics:** two pointers  
**Time:** O(n) · **Space:** O(n) (output)

## Idea
The largest square is at one of the ends (big negatives or big positives). Two pointers: take the end with the larger absolute value, append its square, move that pointer. The result is built largest→smallest, so reverse at the end.

## Alternative
Fill a preallocated array from the back instead of reversing.
