# Source : https://leetcode.cn/problems/intersection-of-two-arrays-ii/
# Author : longchangda
# Time   : 2022-09-03

"""
排序+双指针

思路及算法
如果两个数组是有序的，则可以使用双指针的方法得到两个数组的交集。

首先对两个数组进行排序，然后使用两个指针遍历两个数组。
初始时，两个指针分别指向两个数组的头部。每次比较两个指针指向的两个数组中的数字，
如果两个数字不相等，则将指向较小数字的指针右移一位，
如果两个数字相等，将该数字添加到答案，并将两个指针都右移一位。
当至少有一个指针超出数组范围时，遍历结束。

Time Complexity: O(mlog(m) + nlog(n))
Space Complexity: O(min(m, n))
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        intersection = list()
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                intersection.append(nums1[p1])
                p1 += 1
                p2 += 1

        return intersection
