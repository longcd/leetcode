# Source : https://leetcode.cn/problems/add-binary/
# Author : longcd
# Time   : 2022-09-26

"""
位运算

Time Complexity: O(|a| + |b| + X * max(|a|, |b|))
Space Complexity: O(|a| + |b|)
"""


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
