# Source : https://leetcode.cn/problems/first-unique-character-in-a-string/
# Author : longchangda
# Time   : 2022-09-06

"""
暴力解法

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return -1

        for i in range(n):
            duplicate = False
            for j in range(n):
                if i != j and s[i] == s[j]:
                    duplicate = True
                    break

            if not duplicate:
                return i

        return -1
