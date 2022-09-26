# Source : https://leetcode.cn/problems/add-binary/
# Author : longcd
# Time   : 2022-09-26

"""
模拟

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        carry = 0
        ans = ""
        for i in range(n):
            carry += int(a[len(a) - 1 - i]) if i < len(a) else 0
            carry += int(b[len(b) - 1 - i]) if i < len(b) else 0
            ans += str(carry % 2)
            carry //= 2

        if carry > 0:
            ans += str(carry)

        return ans[::-1]
