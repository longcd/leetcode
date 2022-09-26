# Source : https://leetcode.cn/problems/add-digits/
# Author : longcd
# Time   : 2022-09-26

"""
模拟

Time Complexity: O(log num)
Space Complexity: O(1)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s

        return num
