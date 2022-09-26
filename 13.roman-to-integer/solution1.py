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
        char2int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        n = len(s)
        i = 0
        ret = 0
        while i < n:
            if i < n - 1 and s[i] == "I" and s[i + 1] == "V":
                ret += 4
                i += 2
            elif i < n - 1 and s[i] == "I" and s[i + 1] == "X":
                ret += 9
                i += 2
            elif i < n - 1 and s[i] == "X" and s[i + 1] == "L":
                ret += 40
                i += 2
            elif i < n - 1 and s[i] == "X" and s[i + 1] == "C":
                ret += 90
                i += 2
            elif i < n - 1 and s[i] == "C" and s[i + 1] == "D":
                ret += 400
                i += 2
            elif i < n - 1 and s[i] == "C" and s[i + 1] == "M":
                ret += 900
                i += 2
            else:
                ret += char2int[s[i]]
                i += 1

        return ret
