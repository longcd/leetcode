# Source : https://leetcode.cn/problems/linked-list-cycle/
# Author : longchangda
# Time   : 2022-09-07

"""
哈希表

思路及算法
最容易想到的方法是遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        p = head
        while p:
            if p in seen:
                return True
            seen.add(p)
            p = p.next

        return False
