# Source : https://leetcode.cn/problems/linked-list-cycle/
# Author : longchangda
# Time   : 2022-09-07

"""
快慢指针

思路及算法
「Floyd 判圈算法」（又称龟兔赛跑算法）

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
