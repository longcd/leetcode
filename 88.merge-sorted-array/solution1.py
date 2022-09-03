# Source : https://leetcode.cn/problems/merge-sorted-array/
# Author : longchangda
# Time   : 2022-09-03

"""
直接合并后排序

思路及算法
最直观的方法是先将数组 nums2 放进数组 nums1 的尾部，然后直接对整个数组进行排序。

Time Complexity: O((m + n)log(m + n))，排序序列长度为 m + n，套用快速排序的时间复杂度即可。
Space Complexity: O(log(m + n))，排序序列长度为 m + n，套用快速排序的空间复杂度即可。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
