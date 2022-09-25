# Source : https://leetcode.cn/problems/palindrome-number/
# Author : longcd
# Time   : 2022-09-25

"""
数字转换为字符串

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        # 比较一半
        s = str(x)
        l = len(s)
        h = l // 2
        return s[:h] == s[-1 : -h - 1 : -1]
