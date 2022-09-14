# Source : https://leetcode.cn/problems/add-two-numbers/
# Author : longchangda
# Time   : 2022-09-14

"""
模拟

Time Complexity: O(max(m, n))
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        tail = None
        carry = 0

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            s = n1 + n2 + carry

            if not head:
                head = ListNode(s % 10)
                tail = head
            else:
                tail.next = ListNode(s % 10)
                tail = tail.next

            carry = s // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            tail.next = ListNode()
            tail.next.val = carry

        return head
