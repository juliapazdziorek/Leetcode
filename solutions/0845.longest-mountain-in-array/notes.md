# 845. Longest Mountain in Array (Medium)

**Topics:** two pointers, array  
**Time:** O(n²) worst case (O(n) with skipping) · **Space:** O(1)

## Idea
Find each peak (`arr[i-1] < arr[i] > arr[i+1]`). From the peak expand left while strictly increasing and right while strictly decreasing; the mountain length is `r - l + 1`.

## Pitfalls
- A mountain needs both an up and a down slope — plateaus (equal values) break it.

## Alternative
After expanding from a peak, continue scanning from `r` — every element is then visited O(1) times → O(n).
