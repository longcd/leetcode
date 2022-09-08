# Source : https://leetcode.cn/problems/merge-two-sorted-lists/
# Author : longchangda
# Time   : 2022-09-07

"""
迭代

思路及算法
当 list1 和 list2 都不是空链表时，判断 list1 和 list2 哪一个链表的头节点的值更小，
将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list1 if list1 is not None else list2
        return prehead.next
