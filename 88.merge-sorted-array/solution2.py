# Source : https://leetcode.cn/problems/merge-sorted-array/
# Author : longchangda
# Time   : 2022-09-03

"""
双指针

思路及算法
将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中。

Time Complexity: O(m + n)
Space Complexity: O(m + n)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                result.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                result.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        nums1[:] = result
