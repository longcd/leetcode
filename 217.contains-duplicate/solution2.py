# Source : https://leetcode.cn/problems/contains-duplicate/
# Author : longchangda
# Time   : 2022-09-01

"""
HashTable

For each element in the array, we insert it into the hash table.
If you insert an element and find that it already exists in the hash table,
there are duplicate elements.

Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)

        return False
