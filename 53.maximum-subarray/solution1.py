# Source : https://leetcode.cn/problems/maximum-subarray/
# Author : longchangda
# Time   : 2022-09-01

"""
DP

Time Complexity: O(N)
Space Complexity: O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]
            if nums[i] > max_:
                max_ = nums[i]

        return max_
