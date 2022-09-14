# Source : https://leetcode.cn/problems/3sum/
# Author : longchangda
# Time   : 2022-09-14

"""
排序+双指针

思路及算法
具体算法是先对原数组进行一次排序，然后一层循环固定一个元素，循环内部利用双指针找出剩下的两个元素，这里要特别注意需要去重。

Time Complexity: O(N^2)
Space Complexity: O(logN)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n - 2):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 固定 i，寻找 l 和 r ，使用双指针法
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 去重
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res
