# 121. Best Time to Buy and Sell Stock (Easy)

**Topics:** greedy, array  
**Time:** O(n) · **Space:** O(1)

## Idea
Track the minimum price seen so far. For every day, the best profit selling today is `price - min_price`; keep the maximum of those.

## Pitfalls
- You must buy before you sell — that's why we only use the minimum from the *past*.
