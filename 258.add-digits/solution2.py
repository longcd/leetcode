# Source : https://leetcode.cn/problems/add-digits/
# Author : longcd
# Time   : 2022-09-26

"""
数学

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0
