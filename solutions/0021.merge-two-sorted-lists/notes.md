# 21. Merge Two Sorted Lists (Easy)

**Topics:** linked list, two pointers  
**Time:** O(n + m) · **Space:** O(n + m) (new nodes are created)

## Idea
Dummy head node + a tail pointer. While both lists have nodes, append the smaller value and advance that list. When one list runs out, attach the rest of the other one directly.

## Pitfalls
- Dummy node removes the special case for the first element — return `dummy.next`.

## Alternative
Re-link the existing nodes (`tail.next = list1`) instead of creating new ones → O(1) extra space.
