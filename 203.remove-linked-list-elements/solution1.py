# Source : https://leetcode.cn/problems/remove-linked-list-elements/
# Author : longchangda
# Time   : 2022-09-07

"""
递归

Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
