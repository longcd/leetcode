# Source : https://leetcode.cn/problems/two-sum/
# Author : longchangda
# Time   : 2022-09-02

"""
哈希表

思路及算法
使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N) 降低到 O(1)。

Time Complexity: O(N)，其中 N 是数组中的元素数量。
Space Complexity: O(N)，其中 N 是数组中的元素数量。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            else:
                hash_table[num] = i

        return []
