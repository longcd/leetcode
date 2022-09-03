# Source : https://leetcode.cn/problems/intersection-of-two-arrays-ii/
# Author : longchangda
# Time   : 2022-09-03

"""
哈希表

思路及算法
首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，
然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，
则将该数字添加到答案，并减少哈希表中该数字出现的次数。

为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，
然后遍历较长的数组得到交集。

Time Complexity: O(m + n)
Space Complexity: O(min(m, n))
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        hash_table = dict()
        for num in nums1:
            if hash_table.get(num) is None:
                hash_table[num] = 1
            else:
                hash_table[num] += 1

        intersection = list()
        for num in nums2:
            if hash_table.get(num) is not None and hash_table[num] > 0:
                intersection.append(num)
                hash_table[num] -= 1
                if hash_table[num] == 0:
                    hash_table.pop(num)

        return intersection
