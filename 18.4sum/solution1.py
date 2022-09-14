# Source : https://leetcode.cn/problems/4sum/
# Author : longchangda
# Time   : 2022-09-14

"""
排序+双指针

思路及算法
使用两重循环分别枚举前两个数，然后在两重循环枚举到的数之后使用双指针枚举剩下的两个数。

Time Complexity: O(N^3)
Space Complexity: O(logN)
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        if not nums or len(nums) < 4:
            return res

        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1

        return res
