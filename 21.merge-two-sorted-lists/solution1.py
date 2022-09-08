# Source : https://leetcode.cn/problems/merge-two-sorted-lists/
# Author : longchangda
# Time   : 2022-09-07

"""
递归

思路及算法
list1[0] + mergeTwoLists(list1[1:], list2)    list1[0] < list2[0]
list2[0] + mergeTwoLists(list1, list2[1:])    otherwise

Time Complexity: O(n + m)
Space Complexity: O(n + m)
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
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
