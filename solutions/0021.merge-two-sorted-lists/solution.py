# Created by Jula at 2026/08/06 13:20
# leetgo: 1.4.17
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = list1
        current_node2 = list2
        result_dummy = ListNode()
        result_current = result_dummy

        while current_node1 and current_node2:

            if current_node1.val <= current_node2.val:
                new_node = ListNode(current_node1.val)
                result_current.next = new_node
                result_current = new_node
                current_node1 = current_node1.next
            else:
                new_node = ListNode(current_node2.val)
                result_current.next = new_node
                result_current = new_node
                current_node2 = current_node2.next

        if not current_node1:
            result_current.next = current_node2

        if not current_node2:
            result_current.next = current_node1

        return result_dummy.next

# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)
    print("\noutput:", serialize(ans, "ListNode"))
