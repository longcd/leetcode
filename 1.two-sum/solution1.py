# Source : https://leetcode.cn/problems/two-sum/
# Author : longchangda
# Time   : 2022-09-02

"""
暴力枚举

思路及算法
枚举数组中的每一个数 x，寻找数组中是否存在 target - x。

Time Complexity: O(N^2)，其中 N 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
Space Complexity: O(1)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return []

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
