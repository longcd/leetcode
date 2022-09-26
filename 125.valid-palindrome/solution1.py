# Source : https://leetcode.cn/problems/valid-palindrome/
# Author : longcd
# Time   : 2022-09-26

"""
双指针

Time Complexity: O(|s|)
Space Complexity: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True
