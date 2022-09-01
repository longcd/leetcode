# Source : https://leetcode.cn/problems/contains-duplicate/
# Author : longchangda
# Time   : 2022-09-01

"""
Sort

After sorting numbers from smallest to largest,
the repeating elements of the array must appear in adjacent positions.
Thus, we can scan the sorted array to determine whether two adjacent elements
are equal at a time, and if they are equal, it means that there are duplicate elements.

Time Complexity: O(NlogN)
Space Complexity: O(logN)
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False
