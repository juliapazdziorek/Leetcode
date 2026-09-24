# 347. Top K Frequent Elements (Medium)

**Topics:** hash map, bucket sort  
**Time:** O(n) · **Space:** O(n)

## Idea
Count frequencies. Create buckets where `buckets[f]` holds numbers appearing exactly `f` times (frequency ≤ n, so `n + 1` buckets). Walk buckets from the highest frequency down and collect numbers until you have `k`.

## Alternative
Heap of size k → O(n log k), or sort by count → O(n log n).
