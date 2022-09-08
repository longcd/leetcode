# Source : https://leetcode.cn/problems/remove-linked-list-elements/
# Author : longchangda
# Time   : 2022-09-07

"""
迭代

思路及算法
用 temp 表示当前节点。
如果 temp 的下一个节点不为空且下一个节点的节点值等于给定的 val，则需要删除下一个节点。
如果 temp 的下一个节点的节点值不等于给定的 val，则保留下一个节点，将 temp 移动到下一个节点即可。
当 temp 的下一个节点为空时，链表遍历结束，此时所有节点值等于 val 的节点都被删除。

具体实现方面，由于链表的头节点 head 有可能需要被删除，因此创建哑节点 dummyHead，
令 dummyHead.next=head，初始化 temp=dummyHead，然后遍历链表进行删除操作。
最终返回 dummyHead.next 即为删除操作后的头节点。

Time Complexity: O(n)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return dummyHead.next
