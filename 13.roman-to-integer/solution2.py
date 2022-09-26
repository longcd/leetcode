# Source : https://leetcode.cn/problems/roman-to-integer/
# Author : longcd
# Time   : 2022-09-26

"""
模拟

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = SYMBOL_VALUES[ch]
            if i < n - 1 and value < SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value

        return ans
