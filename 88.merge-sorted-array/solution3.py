# Source : https://leetcode.cn/problems/merge-sorted-array/
# Author : longchangda
# Time   : 2022-09-03

"""
逆向双指针

思路及算法
对数组1、2分别从后向前遍历，并且比较指针指向的元素，将比较大的元素，放到数组1中的末尾，从后往前放进去

Time Complexity: O(m + n)
Space Complexity: O(1)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1

        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                # nums1[tail] = nums1[p1]
                # p1 -= 1
                break
            elif nums1[p1] <= nums2[p2]:
                nums1[tail] = nums2[p2]
                p2 -= 1
            else:
                nums1[tail] = nums1[p1]
                p1 -= 1
            tail -= 1
